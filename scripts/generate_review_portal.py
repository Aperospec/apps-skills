#!/usr/bin/env python3
"""Generate a human-facing static HTML Review Portal from JSON manifests."""

import argparse
import html
import json
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Generate a static Component and Screen Review Portal."
    )
    parser.add_argument(
        "--component-gallery",
        help="Optional component Review Portal manifest JSON",
    )
    parser.add_argument(
        "--screen-gallery",
        help="Optional screen Review Portal manifest JSON",
    )
    parser.add_argument("--output", required=True, help="Output HTML path")
    args = parser.parse_args()
    if not args.component_gallery and not args.screen_gallery:
        parser.error("at least one of --component-gallery or --screen-gallery is required")
    return args


def load_manifest(path, expected_type):
    try:
        data = json.loads(Path(path).read_text(encoding="utf-8"))
    except FileNotFoundError:
        print(f"Error: manifest not found: {path}", file=sys.stderr)
        raise SystemExit(2)
    except json.JSONDecodeError as exc:
        print(f"Error: invalid JSON in '{path}': {exc}", file=sys.stderr)
        raise SystemExit(2)

    if not isinstance(data, dict) or not isinstance(data.get("entries"), list):
        print(
            f"Error: '{path}' must be an object with an 'entries' array.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    portal_type = data.get("portal_type")
    if portal_type not in (expected_type, "combined"):
        print(
            f"Error: '{path}' has portal_type '{portal_type}', expected "
            f"'{expected_type}' or 'combined'.",
            file=sys.stderr,
        )
        raise SystemExit(2)
    return data


def esc(value):
    return html.escape(str(value), quote=True)


def image_panel(label, source):
    if not source:
        return (
            '<div class="image-panel missing"><span>'
            + esc(label)
            + "</span><strong>Not available</strong></div>"
        )
    return (
        '<figure class="image-panel"><figcaption>'
        + esc(label)
        + '</figcaption><img loading="lazy" src="'
        + esc(source)
        + '" alt="'
        + esc(label)
        + '"></figure>'
    )


def link_list(label, values):
    if not values:
        return ""
    links = "".join(
        '<li><a href="' + esc(value) + '">' + esc(value) + "</a></li>"
        for value in values
    )
    return f'<div class="refs"><strong>{esc(label)}</strong><ul>{links}</ul></div>'


def entry_card(entry):
    issues = entry.get("issue_summary") or []
    issue_html = (
        "<ul>" + "".join(f"<li>{esc(issue)}</li>" for issue in issues) + "</ul>"
        if issues
        else '<p class="quiet">No reported exception.</p>'
    )
    status = entry.get("status", "unknown")
    refs = [entry.get("report_ref"), entry.get("registry_ref")]
    refs = [ref for ref in refs if ref]
    human_reason = entry.get("human_review_reason")
    human_block = (
        '<div class="human-callout"><strong>Human decision needed</strong><p>'
        + esc(human_reason or "Review the visual evidence and exception summary.")
        + "</p></div>"
        if entry.get("requires_human_review")
        else ""
    )

    return f"""
    <article class="review-card">
      <header>
        <div>
          <p class="eyebrow">{esc(entry.get("type", "entry"))}</p>
          <h3>{esc(entry.get("name", "Unnamed"))}</h3>
          <p class="figma-name">{esc(entry.get("figma_name") or "")}</p>
        </div>
        <span class="status status-{esc(status)}">{esc(status.replace("_", " "))}</span>
      </header>
      <div class="image-grid">
        {image_panel("Figma reference", entry.get("figma_reference_screenshot"))}
        {image_panel("iOS runtime", entry.get("runtime_screenshot"))}
        {image_panel("Difference", entry.get("diff_image"))}
      </div>
      <div class="conclusion">
        <strong>Agent conclusion</strong>
        <p>{esc(entry.get("agent_conclusion", "No conclusion provided."))}</p>
      </div>
      <div class="issues"><strong>Exceptions</strong>{issue_html}</div>
      {human_block}
      {link_list("Structured records", refs)}
      {link_list("Traceback", entry.get("traceback_refs") or [])}
    </article>
    """


def section(title, subtitle, entries):
    if not entries:
        return ""
    cards = "".join(entry_card(entry) for entry in entries)
    return f"""
    <section>
      <div class="section-heading">
        <p class="eyebrow">Visual delivery</p>
        <h2>{esc(title)}</h2>
        <p>{esc(subtitle)}</p>
      </div>
      <div class="card-stack">{cards}</div>
    </section>
    """


def render(component_entries, screen_entries):
    human_entries = [
        entry
        for entry in component_entries + screen_entries
        if entry.get("requires_human_review")
    ]
    human_cards = "".join(
        f"""
        <article class="exception-card">
          <span class="status status-requires_human_review">requires human review</span>
          <h3>{esc(entry.get("name", "Unnamed"))}</h3>
          <p>{esc(entry.get("human_review_reason") or entry.get("agent_conclusion", ""))}</p>
          <a href="{esc(entry.get("report_ref", "#"))}">Open structured report reference</a>
        </article>
        """
        for entry in human_entries
    )
    human_section = f"""
    <section id="human-review" class="human-section">
      <div class="section-heading">
        <p class="eyebrow">Exceptions only</p>
        <h2>Issues Requiring Human Review</h2>
        <p>Routine implementation is handled by the Agent. These items need a decision.</p>
      </div>
      <div class="exception-grid">
        {human_cards or '<p class="all-clear">No human decision is currently required.</p>'}
      </div>
    </section>
    """

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Figma-to-iOS Review Portal</title>
  <style>
    :root {{
      --ink: #17201d;
      --muted: #64716b;
      --paper: #f4f0e8;
      --card: #fffdf8;
      --line: #d9d2c6;
      --accent: #0f6b55;
      --warning: #a1492a;
      --soft-warning: #fff0e8;
      --shadow: 0 18px 48px rgba(31, 39, 35, .11);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at 12% 0%, rgba(15,107,85,.13), transparent 26rem),
        linear-gradient(135deg, #f8f5ef, var(--paper));
      font-family: "Avenir Next", "Gill Sans", sans-serif;
    }}
    a {{ color: var(--accent); overflow-wrap: anywhere; }}
    .shell {{ width: min(1440px, calc(100% - 32px)); margin: 0 auto; }}
    .hero {{ padding: 72px 0 44px; border-bottom: 1px solid var(--line); }}
    .hero h1 {{ max-width: 900px; margin: 8px 0 14px; font: 700 clamp(42px, 7vw, 92px)/.95 Georgia, serif; }}
    .hero p {{ max-width: 720px; color: var(--muted); font-size: 18px; }}
    .eyebrow {{ margin: 0; color: var(--accent); font-size: 12px; font-weight: 800; letter-spacing: .15em; text-transform: uppercase; }}
    nav {{ display: flex; gap: 18px; flex-wrap: wrap; margin-top: 28px; }}
    nav a {{ font-weight: 700; text-decoration: none; }}
    section {{ padding: 58px 0; }}
    .section-heading {{ max-width: 760px; margin-bottom: 24px; }}
    .section-heading h2 {{ margin: 6px 0; font: 700 clamp(30px, 4vw, 52px)/1 Georgia, serif; }}
    .section-heading > p:last-child {{ color: var(--muted); }}
    .card-stack {{ display: grid; gap: 28px; }}
    .review-card {{ padding: 24px; border: 1px solid var(--line); border-radius: 22px; background: rgba(255,253,248,.94); box-shadow: var(--shadow); }}
    .review-card > header {{ display: flex; justify-content: space-between; gap: 20px; align-items: flex-start; }}
    h3 {{ margin: 5px 0; font-size: 24px; }}
    .figma-name, .quiet {{ margin: 0; color: var(--muted); }}
    .status {{ display: inline-flex; padding: 7px 11px; border-radius: 999px; background: #e6eee9; color: var(--accent); font-size: 12px; font-weight: 800; text-transform: uppercase; }}
    .status-needs_fix, .status-failed {{ background: #fff2d7; color: #8d5a00; }}
    .status-requires_human_review, .status-blocked {{ background: var(--soft-warning); color: var(--warning); }}
    .image-grid {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin: 22px 0; }}
    .image-panel {{ min-height: 180px; margin: 0; border: 1px solid var(--line); border-radius: 14px; overflow: hidden; background: #ede9e0; }}
    .image-panel figcaption, .image-panel > span {{ display: block; padding: 9px 12px; color: var(--muted); font-size: 12px; font-weight: 700; }}
    .image-panel img {{ display: block; width: 100%; min-height: 145px; max-height: 520px; object-fit: contain; background: white; }}
    .image-panel.missing {{ display: grid; place-content: center; text-align: center; color: var(--muted); }}
    .conclusion, .issues, .refs {{ padding-top: 16px; border-top: 1px solid var(--line); }}
    .human-callout {{ margin: 16px 0; padding: 14px 16px; border-left: 4px solid var(--warning); background: var(--soft-warning); }}
    .human-callout p {{ margin-bottom: 0; }}
    .refs ul, .issues ul {{ margin: 8px 0 0; padding-left: 20px; }}
    .human-section {{ border-top: 1px solid var(--line); }}
    .exception-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; }}
    .exception-card, .all-clear {{ padding: 20px; border: 1px solid var(--line); border-radius: 16px; background: var(--card); }}
    footer {{ padding: 30px 0 60px; color: var(--muted); border-top: 1px solid var(--line); }}
    @media (max-width: 800px) {{
      .hero {{ padding-top: 48px; }}
      .image-grid {{ grid-template-columns: 1fr; }}
      .review-card > header {{ flex-direction: column; }}
    }}
  </style>
</head>
<body>
  <header class="hero">
    <div class="shell">
      <p class="eyebrow">Figma-to-iOS Design Fidelity</p>
      <h1>Review the result, not the construction process.</h1>
      <p>Compare Figma references with rendered iOS output. Internal tokens, schemas, and reports remain available for Agent traceback.</p>
      <nav>
        <a href="#components">Component Review</a>
        <a href="#screens">Screen Review</a>
        <a href="#human-review">Human Review Exceptions</a>
      </nav>
    </div>
  </header>
  <main class="shell">
    <div id="components">{section("Component Review", "Local component-library results and automatic quality status.", component_entries)}</div>
    <div id="screens">{section("Screen Review", "Assembled screens compared with their Figma references.", screen_entries)}</div>
    {human_section}
  </main>
  <footer><div class="shell">Generated by the Design Fidelity Kit. Pixel differences are supporting evidence, not the sole acceptance signal.</div></footer>
</body>
</html>
"""


def main():
    args = parse_args()
    component_entries = []
    screen_entries = []
    if args.component_gallery:
        component_entries = load_manifest(args.component_gallery, "component")["entries"]
    if args.screen_gallery:
        screen_entries = load_manifest(args.screen_gallery, "screen")["entries"]

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        render(component_entries, screen_entries),
        encoding="utf-8",
    )
    print(
        f"Created Review Portal: {output_path} "
        f"({len(component_entries)} components, {len(screen_entries)} screens)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


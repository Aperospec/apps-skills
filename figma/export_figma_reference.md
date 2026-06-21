# Export Figma Reference Screenshots

Reference screenshots are the visual source of truth. Export the exact component variant, state, or screen frame used by the target task.

## Manual Figma UI Export

1. Select the exact component, variant, or frame.
2. Confirm theme, locale content, dimensions, and state.
3. Add an export setting at the required scale.
4. Export PNG.
5. Save it under the target project's configured `references/` directory.
6. Record the node ID and output path in the relevant inventory, registry, and report.

## Figma API Export

Use placeholders only:

```bash
curl --fail --silent --show-error \
  --header "X-Figma-Token: FIGMA_API_TOKEN" \
  "https://api.figma.com/v1/images/FIGMA_FILE_KEY?ids=FIGMA_NODE_ID&format=png&scale=1"
```

The response contains a temporary image URL. Download it to the target project's configured reference path. Do not commit `FIGMA_API_TOKEN`, log it, or place it in reports.

Verify that the exported node ID, scale, dimensions, theme, content, and state match the runtime capture. MCP structure is not a replacement for this image.


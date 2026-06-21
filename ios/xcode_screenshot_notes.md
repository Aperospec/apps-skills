# Xcode Screenshot Notes

- Replace `APP_SCHEME`, `SIMULATOR_NAME`, `SCREEN_NAME`, and `OUTPUT_PATH`.
- Record Xcode, iOS Simulator, and OS versions when renderer differences matter.
- Disable unrelated transient overlays, debug banners, and animations before capture.
- Wait for fonts, images, data, and loading states to settle.
- Keep status bar, NavigationBar, TabBar, and Safe Area treatment consistent with Figma.
- Use deterministic fixture data where the target project permits it.
- Restore any temporary capture-only route or fixture after verification.
- Do not force a SwiftUI preview or UIKit test harness onto a project that uses another established approach.

Build and capture commands are project-specific. This kit intentionally does not hardcode a scheme or architecture.


# Capture iOS Runtime Screenshots

Capture the actual rendered result from the external target project. Do not assume SwiftUI, UIKit, an existing UI-test target, or a specific snapshot library.

Match the reference's device dimensions, scale, OS conditions, locale, color scheme, content, and UI state.

## Xcode UI Test

If the target project already has suitable UI tests, navigate to `SCREEN_NAME`, wait for stable rendering, capture an attachment, and export it to `OUTPUT_PATH`. Do not create a new test architecture solely because this kit mentions UI tests.

## Simulator

Boot and run the project's selected destination, then capture:

```bash
xcrun simctl io booted screenshot OUTPUT_PATH
```

Use the target project's own build and launch process with `APP_SCHEME` and `SIMULATOR_NAME`.

## Snapshot Testing

If the project already uses snapshot testing, add a scoped fixture for the required component variant, state, or screen. Configure the same dimensions, locale, theme, and data as the Figma reference.

Component captures should isolate the component without adding visual padding that is absent from the Figma reference.


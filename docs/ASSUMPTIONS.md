# Assumptions

- The repository `realagiorganization/enchanted` contains an iOS app built with Swift/SwiftUI.
- Authentication providers to be added are GitHub OAuth and Discord OAuth using standard OAuth 2.0 flows.
- RevenueCat is the chosen subscription backend for in-app purchases and entitlement management.
- The app will support at least one recurring subscription tier with optional trial.
- GitHub Actions and Fastlane are acceptable CI/CD tooling for TestFlight deployment.
- No existing auth or subscription implementation fully satisfies the requested features.
- The BDD suite can be expressed as Gherkin-style feature files with a lightweight local runner.
- VHS is not available in the container, so the BDD GIF was generated via Pillow while CI uses the VHS action.
- The TestFlight release workflow uses the `Enchanted` scheme in `Enchanted.xcodeproj`.
- App Store Connect API key values are provided via GitHub Actions secrets and the key content is base64-encoded.
- Added CI simulator build lane assumes Xcode device "iPhone 15" is available on GitHub macOS runners.
- GitHub Pages screenshot workflow serves repo root at port 4173 and captures landing page; assumes docs are static and load without extra build step.
- `fastlane ios ci_build` is invoked via `bundle exec` when Gemfile exists; falls back to global fastlane otherwise.

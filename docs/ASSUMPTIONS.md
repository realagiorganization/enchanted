# Assumptions

- iOS app is built with Xcode and uses Fastlane-compatible signing.
- RevenueCat will be used for subscription management with standard offerings.
- GitHub and Discord OAuth will be handled via external provider (e.g. Auth0/Firebase) later; this work covers UI + plumbing only.
- TestFlight deployment uses App Store Connect API key stored in GitHub Secrets.
- GitHub Pages site already exists and only needs verification screenshots, not redesign.

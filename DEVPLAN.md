# Development Plan

## Goals
- Maintain a polished, offline-capable iOS/macOS/visionOS client for private model servers.
- Expand authentication options (GitHub + Discord) and subscription management via RevenueCat.
- Ship reliable CI automation for build, test, and release, plus BDD coverage of core user flows.

## External Dependencies
- Xcode + Swift toolchain (iOS/macOS/visionOS builds)
- Ollama server (local or remote) for inference
- RevenueCat SDK + RevenueCat backend for purchase entitlements
- GitHub OAuth App + Discord OAuth App for authentication
- Fastlane for TestFlight automation
- GitHub Actions for CI/CD
- ngrok (or equivalent) for exposing local servers in testing

## Milestones
1. Baseline health checks, documentation alignment, and CI badges surfaced in README.
2. Authentication and account linking UI (GitHub + Discord) with device Keychain storage.
3. RevenueCat purchase, entitlement sync, and plan management UI.
4. End-to-end BDD coverage of principal user journeys (auth, subscriptions, chat, offline).
5. CI automation for build + test, BDD suite with VHS recording, and TestFlight releases via Fastlane.

## Implementation Steps
1. Audit the existing settings, onboarding, account, and upgrade surfaces to identify insertion points for auth, subscriptions, and entitlement diagnostics.
2. Add OAuth flow scaffolding for GitHub and Discord (PKCE + ASWebAuthenticationSession), persist tokens in Keychain, and surface linked-provider state in account UI.
3. Build the plan purchase/management screen using RevenueCat offerings (purchase, restore, upgrade/downgrade, grace-state messaging) and expose entitlement health in settings.
4. Update settings/upgrade UX to expose current plan status, renewal controls, and troubleshooting links for login/subscription issues.
5. Expand BDD coverage for onboarding, auth, subscription lifecycle, server configuration, messaging, multimodal prompts, and offline usage.
6. Wire the BDD suite into GitHub Actions with VHS recording, publish badges + GIF in README, and capture GitHub Pages screenshot when docs/site change.
7. Align CI for simulator build + test validation and TestFlight releases via Fastlane; document required secrets and simulator targets in README/ASSUMPTIONS.

## Validation
- Run the BDD suite locally and in CI (`python scripts/bdd/run_bdd.py`).
- Manual QA on iOS and macOS: auth, subscription lifecycle, chat flows, offline behavior.
- Release dry-runs using Fastlane lanes in CI.

## Risks and Mitigations
- OAuth callback handling varies per platform: document redirect schemes and test per target.
- RevenueCat entitlement drift: add diagnostics in settings and log reconciliation.
- CI signing failures: centralize certificates/profiles and rotate secrets regularly.

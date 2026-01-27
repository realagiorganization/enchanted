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
1. Baseline health checks and documentation alignment.
2. Authentication and account linking UI (GitHub + Discord).
3. RevenueCat purchase and plan management UI.
4. End-to-end BDD coverage of principal user journeys.
5. CI automation for BDD suite and releases.

## Implementation Steps
1. Audit the existing settings, onboarding, and account screens to identify insertion points for auth and subscriptions.
2. Add OAuth flow scaffolding for GitHub and Discord, including token storage and account linking state.
3. Build the plan purchase/management screen using RevenueCat entitlements and offerings.
4. Update settings/upgrade UX to expose current plan status and renewal controls.
5. Expand BDD coverage for onboarding, server configuration, messaging, multimodal prompts, and offline usage.
6. Wire the BDD suite into GitHub Actions, publish a badge, and generate a GIF demo recording.
7. Align CI for TestFlight releases via Fastlane and document required secrets.

## Validation
- Run the BDD suite locally and in CI (`python scripts/bdd/run_bdd.py`).
- Manual QA on iOS and macOS: auth, subscription lifecycle, chat flows, offline behavior.
- Release dry-runs using Fastlane lanes in CI.

## Risks and Mitigations
- OAuth callback handling varies per platform: document redirect schemes and test per target.
- RevenueCat entitlement drift: add diagnostics in settings and log reconciliation.
- CI signing failures: centralize certificates/profiles and rotate secrets regularly.

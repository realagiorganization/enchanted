# Dev Plan: Auth UI + Subscriptions

## Scope
Add GitHub and Discord login UI/flows and a RevenueCat-powered plan purchase and management screen for the Enchanted iOS app.

## Authentication

### Providers
- GitHub OAuth
- Discord OAuth

### Implementation
- Use ASWebAuthenticationSession for OAuth flows.
- Backend-less first approach using OAuth implicit/PKCE where supported.
- Securely store tokens using Keychain.
- Normalize provider identities into a single local `UserAccount` model.

### UI
- Login screen with provider buttons (GitHub, Discord).
- Account screen showing linked provider and logout.
- Error and cancellation handling states.

## Subscriptions (RevenueCat)

### Setup
- Configure RevenueCat project with App Store Connect.
- Define entitlements and offerings.
- Add RevenueCat SDK to the app.

### Purchase Flow
- Plans screen listing available offerings.
- Purchase, restore, and manage subscription actions.
- Receipt validation handled by RevenueCat.

### State Handling
- Observe entitlement changes via RevenueCat listener.
- Persist subscription state locally for offline UX.

## Edge Cases
- User logs in after purchase: reconcile entitlements.
- Provider logout without subscription loss.
- Restore purchases on new device.

## Analytics & Logging
- Track login success/failure by provider.
- Track purchase funnel events.

## Security
- Minimal token scopes.
- No token logging.
- Keychain access with device-only accessibility.

## Deliverables
- Login UI with GitHub/Discord.
- Account management screen.
- Subscription plans & management screen.
- Documentation for configuration and release.


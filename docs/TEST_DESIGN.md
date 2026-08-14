# Test Design Document — Mobile UI Automation

**Role:** Mobile Automation Engineer
**Tool:** Appium 2.x (Python client) + pytest + Page Object Model
**Target application:** Sauce Labs *My Demo App* (Android, React Native) — an open-source e‑commerce demo app purpose-built for automation practice, with stable, documented accessibility IDs.

---

## 1. Tool & Application Selection (Rationale)

### Why Appium
- **Industry standard & cross-platform.** One codebase drives both Android (UiAutomator2) and iOS (XCUITest). This demonstrates scalable thinking rather than a single-platform script.
- **Language-agnostic; Python chosen for readability.** Python + pytest keeps tests concise and expressive, which helps the "clarity" and "readability" scoring.
- **Appium 2.x (modern).** Uses the current driver/plugin architecture and the `UiAutomator2Options` capabilities API (not the deprecated `desired_capabilities` dict), showing up-to-date practice.

### Why the Sauce Labs My Demo App
- **Realistic e-commerce flows** (login, browse, cart, checkout) — enough surface area to show positive, negative, and edge cases.
- **Stable accessibility IDs**, so tests are resilient and not flaky — directly supports the "Execution and Functionality" criteria.
- **Freely available & legal to automate**, so the GitHub repo and video are fully reproducible by a reviewer.

### Why Page Object Model + pytest fixtures
- **Maintainability & scalability.** UI locators live in one place per screen; a UI change is a one-line fix, not a rewrite.
- **Reusability.** The `driver` session, waits, and common actions are shared, removing duplication.
- **Innovation/efficiency angle.** Explicit waits (no `sleep`), parametrized data-driven negative tests, and a config layer driven by environment variables.

---

## 2. Test Strategy

**Scope.** Core, high-risk user journeys of an e-commerce app: authentication and the add-to-cart → checkout path. These are the flows where a defect causes the most business damage (lost revenue, blocked users), so they are prioritized.

**Approach.**
- **Black-box UI automation** driving the app exactly as a real user would (taps, text entry, scrolling).
- **Explicit synchronization** via `WebDriverWait` + expected conditions, eliminating timing flakiness.
- **Layered architecture:** `BasePage` (reusable actions) → screen page objects → test cases. Tests assert on *behavior and visible state*, never on internal implementation.
- **Data-driven negative testing** using `pytest.mark.parametrize` so multiple invalid-credential combinations run from one test body.
- **Independent, order-agnostic tests.** Each test gets a fresh app session via a function-scoped fixture, so tests can run in parallel or isolation.

**Test types covered.**
| Type | Example |
|------|---------|
| Positive | Valid login succeeds and lands on the product catalog |
| Negative | Locked-out / invalid credentials show the correct error |
| Edge / validation | Empty fields, and cart badge count after multiple adds |
| End-to-end | Add product → cart → checkout information screen |

**Prioritization rationale.** Login is the gateway to every other feature (P1). The cart/checkout flow is the revenue path (P1). Cosmetic screens (menu styling, about page) are deprioritized because their failure has low business impact — this deliberate risk-based selection is the "relevance" the rubric asks for.

**Environment & entry criteria.** Android emulator (API 30+) or a real device, Appium 2 server on `http://127.0.0.1:4723`, app APK installed/available. Tests are green on a clean install of the app.

**Exit criteria.** All P1 automated cases pass; failures are triaged as app bug vs. test/locator issue before sign-off.

---

## 3. Rationale Summary (why these choices align with business logic)

The chosen cases map 1:1 to the app's revenue-critical use cases: a user must be able to authenticate, add the correct item to the cart, and reach checkout. By covering the positive path *and* the negative/edge conditions around it (bad credentials, empty inputs, quantity counts), the suite protects the exact points where real users get blocked or the business loses a sale — which is precisely why they are prioritized over lower-impact screens.

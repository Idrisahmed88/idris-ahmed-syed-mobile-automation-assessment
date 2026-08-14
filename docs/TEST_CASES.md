# Test Cases — Sauce Labs My Demo App (Android)

Format: ID · Title · Priority · Preconditions · Steps · Expected Result · Type

Standard test user (Sauce Labs demo): `bob@example.com` / `10203040`
Locked-out user: `alice@example.com` / `10203040`

---

## TC-01 — Valid login (⭐ automated in video)
- **Priority:** P1
- **Type:** Positive
- **Preconditions:** App installed and on a fresh launch.
- **Steps:**
  1. Open the side menu.
  2. Tap "Log In".
  3. Enter username `bob@example.com`.
  4. Enter password `10203040`.
  5. Tap the Login button.
- **Expected result:** Login succeeds; the products/catalog screen is displayed with at least one product visible.

## TC-02 — Login with invalid credentials
- **Priority:** P1
- **Type:** Negative (data-driven)
- **Preconditions:** On the login screen.
- **Steps:**
  1. Enter an invalid username and/or password (see data set below).
  2. Tap Login.
- **Data set:**
  | username | password | expected error |
  |----------|----------|----------------|
  | `wrong@example.com` | `10203040` | credentials-do-not-match message |
  | `bob@example.com` | `wrongpass` | credentials-do-not-match message |
  | `alice@example.com` (locked) | `10203040` | account-locked message |
- **Expected result:** User is not logged in; the appropriate error message is shown.

## TC-03 — Empty-field validation
- **Priority:** P2
- **Type:** Edge / validation
- **Preconditions:** On the login screen.
- **Steps:**
  1. Leave username and password blank.
  2. Tap Login.
- **Expected result:** Inline validation errors ("Username required" / "Password required") appear; no navigation occurs.

## TC-04 — Add a product to the cart (⭐ automated in video)
- **Priority:** P1
- **Type:** Positive / end-to-end
- **Preconditions:** App launched (login optional for this app's catalog).
- **Steps:**
  1. From the products list, open the first product.
  2. Tap "Add To Cart".
  3. Open the cart.
- **Expected result:** The cart badge shows `1`; the selected product appears in the cart with the correct name and price.

## TC-05 — Cart badge reflects multiple items
- **Priority:** P2
- **Type:** Edge
- **Preconditions:** On the products screen.
- **Steps:**
  1. Add product A to the cart.
  2. Return and add product B to the cart.
- **Expected result:** Cart badge shows `2`; both items are listed in the cart.

## TC-06 — Proceed to checkout requires login / reaches checkout info
- **Priority:** P1
- **Type:** End-to-end
- **Preconditions:** At least one item in the cart.
- **Steps:**
  1. Open the cart.
  2. Tap "Proceed To Checkout".
- **Expected result:** The app routes to the login screen (if not authenticated) or directly to the checkout/address information screen — the checkout flow is entered successfully.

---

**Coverage summary:** positive (TC-01, TC-04), negative (TC-02), edge/validation (TC-03, TC-05), end-to-end (TC-06). The two starred cases (TC-01, TC-04) are the ones demonstrated live in the coding video.

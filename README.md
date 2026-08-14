# Mobile UI Automation — Appium + Python + pytest

Automated UI tests for the **Sauce Labs My Demo App (Android)**, built with
**Appium 2**, **pytest**, and the **Page Object Model**.

Submission for the Mobile Automation Engineer assessment. See
[`docs/TEST_DESIGN.md`](docs/TEST_DESIGN.md) for the design & strategy and
[`docs/TEST_CASES.md`](docs/TEST_CASES.md) for the written test cases.

## Project structure
```
.
├── config/capabilities.py   # Appium capabilities (env-overridable)
├── conftest.py              # pytest driver fixture (fresh session per test)
├── pages/                   # Page Object Model
│   ├── base_page.py         # reusable explicit-wait actions
│   ├── login_page.py
│   ├── products_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py        # TC-01 valid, TC-02 invalid (data-driven)
│   └── test_cart_checkout.py# TC-04 add-to-cart, TC-06 checkout
├── docs/                    # design doc + test cases
├── requirements.txt
└── pytest.ini
```

## Prerequisites
- Node.js + **Appium 2** (`npm i -g appium`) and the UiAutomator2 driver
  (`appium driver install uiautomator2`)
- Android SDK + an emulator (API 30+) or a real device
- Python 3.9+
- The **My Demo App** APK placed at `apps/Android-MyDemoApp.apk`
  (or set `APP_PATH`). Download it from the Sauce Labs sample-app GitHub repo.

## Setup
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
# terminal 1
appium

# terminal 2
pytest                    # all tests
pytest tests/test_login.py::test_valid_login_shows_catalog   # single case
```
An HTML report is written to `reports/report.html`.

## Notes on locators
Accessibility IDs match the Sauce Labs RN demo app. Verify them against your
build with **Appium Inspector**; because of the Page Object Model, any change
is a one-line edit in the relevant `pages/*.py` file.

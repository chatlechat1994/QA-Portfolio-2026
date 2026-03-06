# Test Plan: SauceDemo E-Commerce
**Target Site:** [SauceDemo](https://www.saucedemo.com/)
**Tester:** Frederico Davies
**Date:** February 24, 2026

## 1. Objective
To perform a full functional test of the end-to-end user journey, from secure login to order completion, identifying any blockers in the "Standard" and "Problem" user flows.

## 2. Scope
* **Features:** Login, Product Gallery, Shopping Cart, Checkout Form.
* **Browsers:** Chrome, Firefox.
* **Exclusions:** Performance/Load testing and Payment Gateway integration.

## 3. Test Scenarios
| ID | Scenario | Expected Result |
|---|---|---|
| TS-01 | Login with `standard_user` | User reaches the inventory page. |
| TS-02 | Add item to cart | Cart badge increments correctly. |
| TS-03 | Complete Checkout | User receives "Thank You" confirmation page. |
| TS-04 | `problem_user` Inventory | Verify if images and buttons load correctly. |

## 4. Defect Reporting
All found issues will be logged in the `Bug-Reports.md` file with clear reproduction steps.

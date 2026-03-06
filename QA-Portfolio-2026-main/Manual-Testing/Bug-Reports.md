# Bug Report: Login Authentication Failure 
**Severity:** Critical (Blocker) 
**Priority:** High 
###  Description: The system fails to authenticate the 'problem_user' despite using the correct, provided credentials, preventing any further testing of that user profile.

### Steps to reproduce
1. Navigate to https://www.saucedemo.com/
2. Enter 'problem_user' in the Username field.
3. Enter 'secret_sauce' in the Password field.
4. Click the 'Login' button.

### Actual Result 
Error message displayed: "Epic sadface: Username and password do not match...."

### Screenshot 
![Login Error](https://github.com/user-attachments/assets/5774ade3-fafa-45d9-976a-59a7f50b45ee)




---
## Bug Report: 'Remove' Button Unresponsive on Inventory Page

**Severity:** High  
**Priority:** High  

###  Description
After adding a product to the cart, the "Add to Cart" button correctly changes to a red "Remove" button. However, clicking the "Remove" button has no effect. The item remains in the cart, and the UI does not revert the button state.

### Steps to Reproduce
1. Login as `error_user`.
2. Click 'Add to Cart' on the "Sauce Labs Backpack".
3. Attempt to click the red 'Remove' button that appears.

### Actual Result
The button is not clickable/unresponsive. The cart badge still shows '1' (or '2') and the product remains added.

### Screenshot
![Cart Bug Screenshot](https://github.com/user-attachments/assets/23155b3e-4c24-4bbd-8604-ef3fd93b8f75)

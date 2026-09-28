# QADRS Selenium Automation Project

This project is a Selenium-based browser automation example for testing login and alert flows on demo websites. It combines a few learning-style scripts with a cleaner Page Object Model (POM) structure.

## Project overview

The code demonstrates:

- Browser automation with Selenium WebDriver
- Login test automation on `https://demoblaze.com/`
- Alert handling on `https://demo.automationtesting.in/Alerts.html`
- Different waiting strategies (`time.sleep`, implicit wait, explicit wait)
- Page Object Model structure for reusable UI logic
- Unit tests using `unittest`

## Folder structure

```text
qadrs/
|-- allclasscodes/
|   |-- AlertHandling.py
|   |-- explicitwait.py
|   |-- firstday.py
|   |-- firstwait.py
|-- locator/
|   |-- Locator.py
|-- pages/
|   |-- LoginPage.py
|-- testcases/
|   |-- test_firstwait.py
|   |-- test_login.py
|-- readme.md
```

## Main components

### 1) `locator/Locator.py`
This file stores all reusable UI element locators as class variables.

```python
class Locate:
    login_nav_id = "login2"
    username_id = "loginusername"
    password_id = "loginpassword"
    button_xpath = '//*[@id="logInModal"]/div/div/div[3]/button[2]'
```

Why this matters:

- Keeps selectors in one place
- Makes tests easier to maintain
- Prevents hardcoding locators across multiple files

### 2) `pages/LoginPage.py`
This is the Page Object Model layer. Instead of writing browser actions directly in the test, the page class wraps those actions.

Key parts:

- `__init__(driver)`: stores the browser instance
- `get_login_nav()`: finds the login button
- `click_login_nav()`: clicks it
- `get_username()`: locates the username field
- `enter_username(username)`: types username
- `get_password()`: locates password field
- `enter_password(password)`: types password
- `get_login_button()`: finds the login button in the modal
- `click_login()`: clicks the login button
- `login_function(username, password)`: runs the complete login flow

Example:

```python
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.lc = Locate()

    def login_function(self, username, password):
        self.click_login_nav()
        self.driver.implicitly_wait(10)
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        time.sleep(5)
```

This keeps the test code shorter and more readable.

### 3) `testcases/test_login.py`
This file contains the actual test logic using `unittest`.

It does two tests:

- `test_login`: successful login using valid credentials
- `test_login_negative`: invalid login check, expecting an alert message

```python
class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/")
        self.lp = LoginPage(self.driver)
```

Test flow:

```python
def test_login(self):
    self.lp.login_function("testmorning", "test123")
    expected_result = "Welcome testmorning"
    actual_result = self.driver.find_element(By.ID, "nameofuser").text
    self.assertEqual(expected_result, actual_result, "User was not successful")
```

For negative login:

```python
def test_login_negative(self):
    self.lp.login_function("testmorning", "wrongpassword")
    actual_result = self.driver.switch_to.alert.text
    self.driver.switch_to.alert.accept()
    expected_result = "Wrong password."
    self.assertEqual(expected_result, actual_result, "User was successful")
```

### 4) `testcases/test_firstwait.py`
This is another example test that directly interacts with the browser and uses `implicitly_wait` and `time.sleep`.

```python
self.driver = webdriver.Chrome()
self.driver.maximize_window()
self.driver.get("https://demoblaze.com/")
```

Then it:

- clicks the login button
- waits for the modal
- fills username and password
- clicks login
- waits 5 seconds
- validates the welcome text

```python
welcome_text = self.driver.find_element(By.ID, "nameofuser").text
self.assertEqual("Welcome testmorning", welcome_text)
```

## Learning examples in `allclasscodes`

These files are basic Selenium scripts used to practice browser automation without test frameworks or page objects.

### `allclasscodes/firstday.py`
A simple login script:

- opens Chrome
- opens the Demoblaze homepage
- clicks login
- fills credentials
- clicks login
- waits 5 seconds
- closes the browser

This is a beginner-friendly script showing the core Selenium pattern.

### `allclasscodes/explicitwait.py`
Uses Selenium `WebDriverWait` and `expected_conditions`.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ww = WebDriverWait(driver, 10)
txt_username = ww.until(EC.element_to_be_clickable((By.ID, "loginusername")))
```

This is better than raw `time.sleep` because it waits until the element is actually ready instead of sleeping for a fixed amount of time.

### `allclasscodes/AlertHandling.py`
This script demonstrates browser alert interactions:

- simple alert: accept
- confirmation alert: dismiss
- prompt alert: type text and accept

```python
driver.switch_to.alert.accept()
driver.switch_to.alert.dismiss()
driver.switch_to.alert.send_keys("Testmorning")
```

This is important because many modern web apps use JavaScript alert dialogs, and browser automation must handle them.

## Selenium concepts used in this project

### 1) WebDriver
`webdriver.Chrome()` starts a Chrome browser instance controlled by Selenium.

### 2) Locators
The code uses:

- ID locator: `By.ID`
- XPath locator: `By.XPATH`
- direct attribute lookup: `driver.find_element("id", "login2")`

### 3) Waiting strategies
The project uses multiple waiting methods:

- `time.sleep(5)`
  - simplest; fixed delay
  - can be flaky if pages load slowly or quickly

- `driver.implicitly_wait(10)`
  - tells WebDriver to wait before failing element lookups
  - applies globally

- `WebDriverWait(...).until(...)`
  - more robust than fixed sleeps
  - waits until a condition is true

### 4) Page Object Model (POM)
POM is used in `pages/LoginPage.py`. It separates test logic from UI logic. This makes the framework easier to scale and maintain.

### 5) Unit testing with `unittest`
This project uses Python's built-in test framework:

```python
import unittest
```

`setUp()` runs before each test and `tearDown()` after each test.

## Code flow example

A typical successful login flow in this project looks like this:

1. Launch Chrome browser
2. Navigate to Demoblaze homepage
3. Click the login navigation button
4. Wait for the login modal to appear
5. Enter username
6. Enter password
7. Click login
8. Wait for page response
9. Read the welcome text
10. Compare with expected text
11. Pass/fail result based on assertion

## Dependencies

This project requires Selenium.

Install it with:

```bash
pip install selenium
```

Optional: if you are using a managed environment or virtual environment, activate it before installing dependencies.

## Running tests

From the project root:

```bash
python -m pytest testcases/test_login.py
```

or run with unittest directly:

```bash
python -m unittest testcases.test_login
```

You can also run the older script-based examples directly:

```bash
python allclasscodes/firstday.py
python allclasscodes/explicitwait.py
python allclasscodes/AlertHandling.py
```

## Important notes

- The project is educational and demonstration-focused.
- Some scripts use fixed waits (`time.sleep`) which are less reliable than explicit waits.
- The login tests depend on the demo website being available and stable.
- Browser versions and ChromeDriver compatibility matter. If ChromeDriver does not match the installed Chrome version, browser launch may fail.
- Since this project interacts with a live website, tests may need updates if the site structure changes.

## Best practices for this codebase

To improve the project, the following would be useful:

- Replace fixed `sleep()` calls with explicit waits
- Add test data constants or config files
- Use pytest for cleaner and more scalable test reporting
- Add page classes for other pages (home page, cart page, product page)
- Use environment variables for credentials
- Add logging and screenshots on failure

## Summary

This project is a Selenium automation learning project that covers:

- browser automation basics
- login page workflow automation
- alert handling
- page object model design
- wait strategies
- real-world UI test validation using `unittest`

It is a good starting point for learning end-to-end web UI automation in Python.

## Credits

This project is a practical Selenium automation example built for learning and experimentation.

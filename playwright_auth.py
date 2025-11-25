from copyreg import constructor

from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration'
    )

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    for char in 'user.name@gmail.com':
        page.keyboard.type(char, delay=50)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    for char in 'username':
        page.keyboard.type(char, delay=50)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    for char in 'password':
        page.keyboard.type(char, delay=50)

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='./browser-state.json')

    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')

    page.wait_for_timeout(3000)

from playwright.sync_api import expect


def test_login_with_standard_user(page):
    # 1. Open the SauceDemo login page.
    page.goto("https://www.saucedemo.com/")

    # 2. Type the demo username and password into the two fields.
    page.locator('[data-test="username"]').fill("standard_user")
    page.locator('[data-test="password"]').fill("secret_sauce")

    # 3. Click Login.
    page.locator('[data-test="login-button"]').click()

    # 4. Prove it worked: we landed on the inventory page,
    #    and the page title says "Products".
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_have_text("Products")

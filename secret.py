from playwright.sync_api import sync_playwright
import os


def main():

    with sync_playwright() as p:
        meno = "Jarmil"
        heso = "Admin123"
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://js-trebesin.github.io/playwright-exam/")

        page.fill('input[id="login"]', meno)
        page.fill('input[id="pass"]', heso)

        page.click('button[class="login-btn"]')

        secret = page.locator('p[class="super-secret-text"]')

        print(secret.text_content())

        input("dobre ranko prosim jednicku s hvezdickou")
        browser.close()


if __name__ == "__main__":
    main()

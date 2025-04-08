from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://auditms-uat.haid.com.cn/static/login/login.html")
    page.locator("#userName").click()
    page.locator("#userName").fill("chain")
    page.locator("#userName").press("Tab")
    page.locator("#pwd").fill("123456")
    page.locator("#pwd").press("Enter")
    page.get_by_title("项目管理", exact=True).click()
    page.get_by_title("项目申请", exact=True).click()
    page.get_by_role("link", name="查询项目申请").click()
    page.locator("#searchFormTableCustomize").get_by_text("查询").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

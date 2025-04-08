from playwright.sync_api import Page

# hello1参数来自conftest.py，这里放的是公共调用的
# playwright codegen --target python -o login_test.py -b chromium https://auditms-uat.haid.com.cn/static/login/login.html
def test_baidu(page: Page):
    # page.goto("https://www.baidu.com")
    # page.get_by_role("link", name="新闻").click()
    # expect(page).to_have_title("百度新闻——全球最具影响力的中文新闻媒体")
    # page.get_by_role("link", name="体育").click()
    # expect(page).to_have_title("体育 - 百度新闻")
    # page.get_by_role("link", name="NBA").click()
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

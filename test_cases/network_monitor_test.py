from playwright.sync_api import Playwright,Request
def test_network_monitor(playwright: Playwright) -> None:
    # Request
    def on_context(req: Request) -> None:
        # print(req.timing)
        if "www.baidu.com" in req.url:
         print(req.url)
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # context.on("request", lambda req: print(req.url))
    # context.on("response", lambda res: print(res.url))
    # context.on("request", lambda req: print(req.timing))
    page = context.new_page()
    page.goto("https://www.baidu.com")


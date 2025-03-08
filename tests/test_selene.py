from selene import browser, by, be

def test_github():
    browser.config.window_height = 1080  # высота браузера
    browser.config.window_width = 1920 # ширина браузера
    browser.open('https://github.com/')

    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).click()
    browser.element('#actions-tab').click()
    browser.element(by.partial_text('#278')).should(be.visible)


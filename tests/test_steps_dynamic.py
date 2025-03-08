import allure
from selene import browser, by, be, have

def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.config.window_height = 1080
        browser.config.window_width = 1920
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб actions и ищем нужный номер workflow'):
        browser.element('#actions-tab').click()
        browser.element(by.partial_text('#278')).should(be.visible)


import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_dynamic_steps():
    with allure.step('Открываем главную страницу'):
        browser.config.window_height = 1080  # высота браузера
        browser.config.window_width = 1920 # ширина браузера
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        browser.element('[class="search-input"]').click()
        browser.element('[id="query-builder-test"]').type('eroshenkoam/allure-example').press_enter()

    with allure.step('Переходим по ссылке репозитория'):
        browser.element(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем таб actions'):
        browser.element('#actions-tab').click()

    while allure.step('Ищем нужный номер workflow'):
        browser.element(by.partial_text('#1278')).should(be.visible)

#---------------------------------------------------
#---------------------------------------------------
def test_decorator_steps():
 open_main_page()
 search_for_repository('eroshenkoam/allure-example')
 go_to_repository('eroshenkoam/allure-example')
 open_actions_tab()
 should_see_number('278')


#далее тест пишем так (выше)
@allure.step('Открываем главную страницу')
def open_main_page():
    browser.config.window_height = 1080  # высота браузера
    browser.config.window_width = 1920  # ширина браузера
    browser.open('https://github.com/')

@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    browser.element('[class="search-input"]').click()
    browser.element('[id="query-builder-test"]').type(repo).press_enter()

@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    browser.element(by.link_text('eroshenkoam/allure-example')).click()

@allure.step('Открываем таб actions')
def open_actions_tab():
    browser.element('#actions-tab').click()

@allure.step('Ищем нужный номер workflow {number}')
def should_see_number(number):
    browser.element(by.partial_text('#' + number)).should(be.visible)
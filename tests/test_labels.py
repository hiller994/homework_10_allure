import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s

from tests.test_steps_decorator import open_main_page, search_for_repository, go_to_repository, open_actions_tab, \
    should_see_number


def test_decorator_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Домашнее задание по лекции 10")
    allure.dynamic.story("Разметка тестов всеми аннотациями")
    allure.dynamic.link("https://github.com", name="Testing")

    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_actions_tab()
    should_see_number('278')


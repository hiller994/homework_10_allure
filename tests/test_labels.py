import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


#используется, когда пишутся тесты как требования. В аллюре владка Behaviors

def test_no_labels():
    pass ##
def test_dynamic_labels():
    allure.dynamic.tag("web")
    allure.dynamic.severity(Severity.BLOCKER)
    allure.dynamic.feature("Задачи в репозитории")
    allure.dynamic.story("не авторизованный пользователь не может создать задачу в репозитории")
    allure.dynamic.link("https://github.com", name="Testing")

#для препода это более верная разметка. Получается это комментарии и ийформация в задаче для какого-нибудь теста в аллюре
@allure.tag('critical')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "erosenkoam")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_labels():
    pass
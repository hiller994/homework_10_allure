import json

import allure
from allure import attachment_type

def test_attachment():
    allure.attach('Text content', name='Text', attachment_type=attachment_type.TEXT) #где name это название нашего аттачмента
    #таким образом мы можешь прикрепить какую нибудь текстовую информацию
    allure.attach('<h1>Hello, world</h1>', name='html', attachment_type=attachment_type.HTML) #создаем файл
    allure.attach(json.dumps({"first":1, "second":2}), name="Json", attachment_type=attachment_type.JSON) #создаем файл

    #получается, что данные файлы можно прикреплять к тестам, как описание 
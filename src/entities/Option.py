from importlib import import_module

BASE_ENTITY = import_module('entities.BaseEntity')


class Option(BASE_ENTITY.BaseEntity):
    """
    Класс, представляющий вариант ответа на вопрос

    Свойства:
        option_id (int):            ID варианта ответа
        text (string):              текст ответа
        correct (bool):             True - ответ верный, False - неверный
    """

    def __init__(self,
                 option_id,
                 text,
                 correct):
        self.__option_id = option_id
        self.__text = text
        self.__correct = correct

    @property
    def option_id(self):
        return self.__option_id

    @option_id.setter
    def option_id(self, option_id):
        self.__option_id = option_id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def correct(self):
        return self.__correct

    @correct.setter
    def correct(self, correct):
        self.__correct = correct

    def __json__(self):
        return {
            'option_id': self.__option_id,
            'text': self.__text,
            'correct': self.__correct,
        }

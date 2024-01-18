from importlib import import_module

BASE_ENTITY = import_module('entities.BaseEntity')


class Question(BASE_ENTITY.BaseEntity):
    """
    Класс, представляющий вопрос теста

    Свойства:
        question_id (int):              ID вопроса
        text (str):                     текст вопроса
        points (int):                   кол-во очков за правильный ответ
        options (list<Option>):         варианты ответа
    """

    def __init__(self,
                 question_id,
                 text,
                 points,
                 options):
        self.__question_id = question_id
        self.__text = text
        self.__points = points
        self.__options = options

    @property
    def question_id(self):
        return self.__question_id

    @question_id.setter
    def question_id(self, question_id):
        self.__question_id = question_id

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        self.__text = text

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    @property
    def options(self):
        return self.__options

    @options.setter
    def options(self, options):
        self.__options = options

    def __json__(self):
        return {
            'question_id': self.__question_id,
            'text': self.__text,
            'points': self.__points,
            'options': list(map(
                lambda op: op.__json__(),
                self.__options
            )),
        }

from importlib import import_module

BASE_ENTITY = import_module('entities.BaseEntity')


class Test(BASE_ENTITY.BaseEntity):
    """
    Класс, представляющий тест

    Свойства:
        test_id (int):              ID теста
        title (str):                название теста
        description (str):          описание теста
        questions (list<Question>): список вопросов
    """

    def __init__(self,
                 test_id,
                 title,
                 description,
                 questions):
        self.__test_id = test_id
        self.__title = title
        self.__description = description
        self.__questions = questions

    @property
    def test_id(self):
        return self.__test_id

    @test_id.setter
    def test_id(self, test_id):
        self.__test_id = test_id

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description):
        self.__description = description

    @property
    def questions(self):
        return self.__questions

    @questions.setter
    def questions(self, questions):
        self.__questions = questions

    def __json__(self):
        return {
            'test_id': self.__test_id,
            'title': self.__title,
            'description': self.__description,
            'questions': list(map(
                lambda q: q.__json__(),
                self.__questions
            )),
        }

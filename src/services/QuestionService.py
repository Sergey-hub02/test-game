from importlib import import_module
from random import shuffle, sample

BASE_SERVICE = import_module('services.BaseService')
QUESTION_ENTITY = import_module('entities.Question')


class QuestionService(BASE_SERVICE.BaseService):
    """
    Класс, взаимодействующий с таблицей вопросов теста
    """
    def __init__(self, table, conn, option_service):
        if not option_service:
            raise Exception('Не внедрена зависимость OptionService!')

        super().__init__(table, conn)
        self.__option_service = option_service

    def find(self,
             text='',
             points=0,
             test=0):
        """
        Возвращает вопросы, удовлетворяющий заданным условиям

        Параметры:
            text (str):             текст вопрос
            points (int):           кол-во очков за правильный ответ
            test (int):             ID теста
        """
        query = '''
            SELECT
                "question_id",
                "text",
                "points",
                "test"
            FROM "{}"
            WHERE true
        '''.format(self._table)

        prepared_params = []

        if text:
            query += ' AND "text" = %s'
            prepared_params.append(text)

        if points != 0:
            query += ' AND "points" = %s'
            prepared_params.append(points)

        if test != 0:
            query += ' AND "test" = %s'
            prepared_params.append(test)

        with self._conn.execute(query, prepared_params) as cur:
            rows = cur.fetchall()

            if len(rows) == 0:
                return []

            return list(map(
                lambda q: QUESTION_ENTITY.Question(
                    q['question_id'],
                    q['text'],
                    q['points'],
                    self.__option_service.find(question=q['question_id'])
                ),
                rows
            ))

    def find_by_id(self, question_id):
        """
        Возвращает вопрос с указанным ID

        Параметры:
            question_id (int):          ID вопроса
        """
        if not question_id:
            return None

        query = '''
            SELECT
                "question_id",
                "text",
                "points",
                "test"
            FROM "{}"
            WHERE "question_id" = %s
        '''.format(self._table)

        with self._conn.execute(
            query,
            (question_id,)
        ) as cur:
            row = cur.fetchone()

            if not row:
                return None

            question_options = self.__option_service.find(question=question_id)

            return QUESTION_ENTITY.Question(
                row['question_id'],
                row['text'],
                row['points'],
                question_options
            )

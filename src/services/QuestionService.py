from importlib import import_module
from random import shuffle

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

    def find(self):
        pass

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
            shuffle(question_options)

            return QUESTION_ENTITY.Question(
                row['question_id'],
                row['text'],
                row['points'],
                question_options
            )

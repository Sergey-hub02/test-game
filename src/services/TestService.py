from importlib import import_module

BASE_SERVICE = import_module('services.BaseService')
TEST_ENTITY = import_module('entities.Test')


class TestService(BASE_SERVICE.BaseService):
    """
    Класс, взаимодействующий с таблицей тестов
    """

    def __init__(self, table, conn, question_service):
        if not question_service:
            raise Exception('Не внедрена зависимость QuestionService!')

        super().__init__(table, conn)
        self.__question_service = question_service

    def find(self,
             title='',
             description=''):
        """
        Возвращает все тесты, удовлетворяющие заданным условиям

        Параметры:
            title (str):            название теста
            description (str):      описание теста
        """
        query = '''
            SELECT
                "test_id",
                "title",
                "description"
            FROM "{}"
            WHERE true
        '''.format(self._table)

        prepared_params = []

        if title:
            query += ' AND "title" = %s'
            prepared_params.append(title)

        if description:
            query += ' AND "description" = %s'
            prepared_params.append(description)

        with self._conn.execute(query, prepared_params) as cur:
            rows = cur.fetchall()

            if len(rows) == 0:
                return []

            return list(map(
                lambda t: TEST_ENTITY.Test(
                    t['test_id'],
                    t['title'],
                    t['description'],
                    self.__question_service.find(test=t['test_id'])
                ),
                rows
            ))

    def find_by_id(self, test_id):
        """
        Возвращает тест с указанным ID

        Параметры:
            test_id (int):          ID теста
        """
        if not test_id:
            return None

        query = '''
            SELECT
                "test_id",
                "title",
                "description"
            FROM "{}"
            WHERE "test_id" = %s
        '''.format(self._table)

        with self._conn.execute(query, (test_id,)) as cur:
            row = cur.fetchone()

            if not row:
                return None

            return TEST_ENTITY.Test(
                row['test_id'],
                row['title'],
                row['description'],
                self.__question_service.find(test=test_id)
            )

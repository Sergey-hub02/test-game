from importlib import import_module

BASE_SERVICE = import_module('services.BaseService')
OPTION_ENTITY = import_module('entities.Option')


class OptionService(BASE_SERVICE.BaseService):
    """
    Класс для взаимодействия с таблицей вариантов ответа
    """

    def find(self,
             option_id=0,
             text='',
             correct=None,
             question=0):
        pass

    def find_by_id(self, option_id):
        """
        Возвращает вариант ответа с указанным ID

        Параметры:
            option_id (int):            ID варианта ответа
        """
        query = '''
            SELECT
                "option_id",
                "text",
                "correct"
            FROM "{}"
            WHERE "option_id" = %s
        '''.format(self._table)

        with self._conn.execute(query, (option_id,)) as cur:
            row = cur.fetchone()

            if not row:
                return None

            return OPTION_ENTITY.Option(row['option_id'],
                                        row['text'],
                                        row['correct'])

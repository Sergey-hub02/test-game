from importlib import import_module
from random import shuffle

BASE_SERVICE = import_module('services.BaseService')
OPTION_ENTITY = import_module('entities.Option')


class OptionService(BASE_SERVICE.BaseService):
    """
    Класс для взаимодействия с таблицей вариантов ответа
    """

    def find(self,
             text='',
             correct=None,
             question=0):
        """
        Возвращает варианты ответа, удовлетворяющие заданным условиям

        Параметры:
            text (str):             текст ответа
            correct (bool|None):    True - ответ верный, False - ответ неверный
            question (int):         ID вопроса
        """
        query = ('SELECT'
                 + ' "option_id",'
                 + ' "text",'
                 + ' "correct",'
                 + ' "question"'
                 + f' FROM "{self._table}"'
                 + ' WHERE true')

        prepared_params = []

        if text:
            query += ' AND "text" = %s'
            prepared_params.append(text)

        if correct is not None:
            query += ' AND "correct" = %s'
            prepared_params.append(correct)

        if question != 0:
            query += ' AND "question" = %s'
            prepared_params.append(question)

        with self._conn.execute(query, prepared_params) as cur:
            row = cur.fetchall()

            if len(row) == 0:
                return []

            options = list(map(
                lambda op: OPTION_ENTITY.Option(
                    op['option_id'],
                    op['text'],
                    op['correct']
                ),
                row
            ))

            shuffle(options)
            return options

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

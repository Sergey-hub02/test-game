class BaseService:
    """
    Класс верхнего уровня для всех сервисов

    Свойства:
        table (string):             название таблицы в БД
        conn (psycopg.Connection):  соединение с БД
    """

    def __init__(self, table, conn):
        if not table:
            raise Exception('Не указано название таблицы в БД!')

        if conn is None:
            raise Exception('Не передано соединение с БД!')

        self._table = table
        self._conn = conn

    def __del__(self):
        self._conn.close()

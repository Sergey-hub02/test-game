import psycopg

from psycopg.rows import dict_row

from services.OptionService import OptionService
from services.QuestionService import QuestionService
from services.TestService import TestService

CONNECTION_URL = 'postgresql://postgres:alastor_cool@localhost:5432/test-game'


def main():
    with psycopg.connect(
        CONNECTION_URL,
        row_factory=dict_row
    ) as conn:
        option_service = OptionService('Option', conn)
        question_service = QuestionService('Question', conn, option_service)
        test_service = TestService('Test', conn, question_service)

        for t in test_service.find(title='Тест на знатока серии игр \"Dark Souls\"'):
            print(t)


if __name__ == '__main__':
    main()

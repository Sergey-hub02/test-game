import psycopg

from psycopg.rows import dict_row
from services.OptionService import OptionService
from services.QuestionService import QuestionService

CONNECTION_URL = 'postgresql://postgres:alastor_cool@localhost:5432/test-game'


def main():
    with psycopg.connect(
        CONNECTION_URL,
        row_factory=dict_row
    ) as conn:
        option_service = OptionService('Option', conn)
        question_service = QuestionService('Question', conn, option_service)

        print(question_service.find_by_id(5))


if __name__ == '__main__':
    main()

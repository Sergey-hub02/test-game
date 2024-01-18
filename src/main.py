import psycopg

from psycopg.rows import dict_row
from services.OptionService import OptionService

CONNECTION_URL = 'postgresql://postgres:alastor_cool@localhost:5432/test-game'


def main():
    with psycopg.connect(
        CONNECTION_URL,
        row_factory=dict_row
    ) as conn:
        option_service = OptionService('Option', conn)

        for option in option_service.find(question=3):
            print(option)


if __name__ == '__main__':
    main()

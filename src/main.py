import psycopg

from psycopg.rows import dict_row

from services.OptionService import OptionService
from services.QuestionService import QuestionService
from services.TestService import TestService

from entities.Player import Player

CONNECTION_URL = 'postgresql://postgres:alastor_cool@localhost:5432/test-game'


def main():
    with psycopg.connect(
        CONNECTION_URL,
        row_factory=dict_row
    ) as conn:
        option_service = OptionService('Option', conn)
        question_service = QuestionService('Question', conn, option_service)
        test_service = TestService('Test', conn, question_service)

        print('========== ДОБРО ПОЖАЛОВАТЬ ==========')
        name = input('Введите ваше имя: ')
        player = Player(name)

        print()
        print('========== ДОСТУПНЫЕ ТЕСТЫ ==========')

        tests = test_service.find()

        for i, test in enumerate(tests):
            print(f'{i + 1}) {test.title}')
            print(test.description)
            print()

        test_index = int(input(f'Ваш выбор (1-{len(tests)}): '))
        selected_test = tests[test_index - 1]

        print()
        print('========== НАЧАЛО ТЕСТА ==========')

        for i, question in enumerate(selected_test.questions):
            player.print_player_info()

            print(f'Вопрос №{i + 1}')
            print(question.text)

            print()
            print('Варианты ответа:')

            for j, option in enumerate(question.options):
                print(f'{j + 1}) {option.text}')
            print()

            option_index = int(input(f'Ваш ответ (1-{len(question.options)}): '))
            selected_option = question.options[option_index - 1]

            print()

            if not selected_option.correct:
                print('----- ОТВЕТ НЕВЕРНЫЙ -----')
                print()
                break

            print('----- ОТВЕТ ВЕРНЫЙ -----')

            player.points += question.points
            print()

        player.print_player_info()


if __name__ == '__main__':
    main()

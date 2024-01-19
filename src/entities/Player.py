class Player:
    """
    Класс, представляющий игрока, проходящего тест

    Свойства:
        name (str):             имя игрока
        score (int):            кол-во очков
    """

    def __init__(self, name):
        self.__name = name
        self.__points = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, points):
        self.__points = points

    def print_player_info(self):
        """
        Выводит на экран имя игрока и его очки
        """
        print('Игрок:', self.__name)
        print('Кол-во очков:', self.__points)
        print()

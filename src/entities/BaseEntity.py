from json import dumps


class BaseEntity:
    """
    Класс верхнего уровня для всех сущностей
    """

    def __str__(self):
        return dumps(self.__json__(),
                     ensure_ascii=False,
                     indent=4)

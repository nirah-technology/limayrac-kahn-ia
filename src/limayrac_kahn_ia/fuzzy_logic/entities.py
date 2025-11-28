class LeftSideTrapeze:
    def __init__(self, min_up_tray: float, max_up_tray: float, max_right_rope: float):
        self.__min_up_tray: float = min_up_tray
        self.__max_up_tray: float = max_up_tray
        self.__max_right_rope: float = max_right_rope

    @property
    
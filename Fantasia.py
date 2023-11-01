from typing import Optional, Dict

from src.UserData import UserData
from FantasiaSetting import USER_COLORS


class Fantasia:
    def __init__(self):
        self._user_datas: Dict[str, UserData] = {user_color: UserData.create_object(user_color) for user_color in USER_COLORS}
        self._round = 1
        self._turn = 0  # 0 ~ 5는 각각의 유저에 대응
        self._tradeable_animals = {}

    def get_current_turn_user(self) -> UserData:
        return self._user_datas.get([key for key in self._user_datas.keys()][self._turn])

    def change_turn(self):
        if self._turn == 5:
            self._turn = 0

        else:
            self._turn += 1

    def round_change(self):
        self._round += 1

        for user_data in self._user_datas.values():
            for herb_data in user_data.herbs.values():
                herb_data.round = self._round

    def set_tradeable_animal(self, name: str, level: int):
        self._tradeable_animals.update({name: level})

    def init_tradeable_animal(self):
        self._tradeable_animals.clear()



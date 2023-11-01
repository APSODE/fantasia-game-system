from typing import Optional, Dict

from src.UserData import UserData
from FantasiaSetting import USER_COLORS, HERB_CARD, ANIMAL_CARD, TOOL_CARD


class Fantasia:
    def __init__(self):
        self._user_datas: Dict[str, UserData] = {user_color: UserData.create_object(user_color) for user_color in USER_COLORS}
        self._round = 1
        self._tradeable_animals = {}

    def get_user(self, color: str) -> UserData:
        return self._user_datas.get(color)

    def round_change(self):
        self._round += 1

        for user_data in self._user_datas.values():
            for herb_data in user_data.herbs.values():
                herb_data.round = self._round

        self.apply_profit()

    def set_tradeable_animal(self, name: str, level: int):
        self._tradeable_animals.update({name: level})

    def init_tradeable_animal(self):
        self._tradeable_animals.clear()

    def apply_profit(self):
        # 월급 지급 코드 (유저 전체)
        for user_dto in self._user_datas.values():
            total_profit = 0
            for tool_dto in user_dto.tools.values():
                if tool_dto.is_activated:
                    total_profit += tool_dto.profit

            for animal_dtos in user_dto.animals.values():
                for animal_dto in animal_dtos:
                    if animal_dto.amount > 0:
                        total_profit += animal_dto.profit

            total_profit -= user_dto.get_drugs_debuff()

    @property
    def round(self) -> int:
        return self._round



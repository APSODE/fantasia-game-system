from typing import Optional, Dict, List

from src.UserData import UserData
from FantasiaSetting import USER_COLORS, HERB_CARD, ANIMAL_CARD, TOOL_CARD, DEFAULT_TRADEABLE_ANIMALS


class Fantasia:
    def __init__(self):
        self._user_datas: Dict[str, UserData] = {user_color: UserData.create_object(user_color) for user_color in USER_COLORS}
        self._round = 1
        # 라운드 별로 판매 가능한 마법 동물을 수정하려면 DEFAULT_TRADEABLE_ANIMALS의 선언부로 들어가서 수정하면 됨
        self._tradeable_animals: Dict[str, List[Dict[str, int]]] = DEFAULT_TRADEABLE_ANIMALS

    def get_user(self, color: str) -> UserData:
        return self._user_datas.get(color)

    def round_change(self):
        self._round += 1

        for user_data in self._user_datas.values():
            for herb_data in user_data.herbs.values():
                herb_data.round = self._round

        self.apply_profit()
        self.init_tradeable_animal()

    def set_tradeable_animal(self, name: str, level: int):
        self._tradeable_animals.update({name: level})

    def init_tradeable_animal(self):
        self._tradeable_animals.clear()

    def apply_profit(self):
        # 월급 지급 코드 (유저 전체)
        for user_dto in self._user_datas.values():
            user_dto.mana += user_dto.get_current_round_profit()

    @property
    def round(self) -> int:
        return self._round

    @property
    def tradeable_animals(self) -> Dict[str, List[Dict[str, int]]]:
        return self._tradeable_animals

    @tradeable_animals.setter
    def tradeable_animals(self, value: Dict[str, List[Dict[str, int]]]):
        self._tradeable_animals = value

    def is_tradeable(self, animal_name: str, animal_level: int) -> bool:
        for animals in self._tradeable_animals.get(f"{self._round}"):
            if animals.get(animal_name) and animals.get(animal_name) == animal_level:
                return True

        return False




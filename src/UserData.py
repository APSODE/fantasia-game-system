from typing import Optional, List, Dict
from src.MagicalToolData import MagicalToolData
from src.MagicalAnimalData import MagicalAnimalData
from src.MagicalHerbData import MagicalHerbData
from FantasiaSetting import HERB_COST_DATA, ANIMAL_COST_DATA, TOOL_COST_DATA


class UserData:
    def __init__(self,
                 color: str,
                 mana: int,
                 drugs: int,
                 ):

        self._color = color
        self._mana = mana
        self._drugs = drugs
        self._herbs = {
            "캐오닌": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("캐오닌")),
            "바카스": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("바카스")),
            "코로롱": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("코로롱")),
            "버들": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("버들")),
            "번개": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("번개")),
            "버프": MagicalHerbData.create_initial_value(HERB_COST_DATA.get("버프")),
        }
        self._animals = {
            "퍼프": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("퍼프")),
            "주디": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("주디")),
            "위즈": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("위즈")),
            "주비": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("주비")),
            "유니콘": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("유니콘")),
            "불사조": MagicalAnimalData.create_initial_value(ANIMAL_COST_DATA.get("불사조")),
        }
        self._tools = {
            "마법부적": MagicalToolData.create_object(**TOOL_COST_DATA.get("마법부적")),
            "마법지도": MagicalToolData.create_object(**TOOL_COST_DATA.get("마법지도")),
            "마법양초": MagicalToolData.create_object(**TOOL_COST_DATA.get("마법양초")),
            "마법거울": MagicalToolData.create_object(**TOOL_COST_DATA.get("마법거울")),
            "지팡이": MagicalToolData.create_object(**TOOL_COST_DATA.get("지팡이")),
            "빗자루": MagicalToolData.create_object(**TOOL_COST_DATA.get("빗자루"))
        }

    @staticmethod
    def create_object(color: str, mana: int = 300, drugs: int = 0) -> "UserData":
        return UserData(
            color = color,
            mana = mana,
            drugs = drugs
        )


    @property
    def color(self):
        return self._color

    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, value: int):
        self._mana = value

    @property
    def drugs(self) -> int:
        return self._drugs

    @drugs.setter
    def drugs(self, value: int):
        self._drugs = value

    @property
    def herbs(self) -> Dict[str, MagicalHerbData]:
        return self._herbs

    @herbs.setter
    def herbs(self, value: Dict[str, MagicalHerbData]):
        self._herbs = value

    @property
    def animals(self) -> Dict[str, List[MagicalAnimalData]]:
        return self._animals

    @animals.setter
    def animals(self, value: Dict[str, List[MagicalHerbData]]):
        self._animals = value

    @property
    def tools(self) -> Dict[str, MagicalToolData]:
        return self._tools

    @tools.setter
    def tools(self, value: Dict[str, MagicalToolData]):
        self._tools = value

    def sell_herb(self, name: str, amount: int):
        herb_dto = self._herbs.get(name)

        if herb_dto.amount >= amount:
            herb_dto.amount -= amount
            self._mana += herb_dto.cost * amount

        else:
            raise ValueError("해당 허브를 소지하고 있지 않거나 갯수가 부족합니다.")

    def buy_herb(self, name: str, amount: int):
        herb_dto = self._herbs.get(name)
        total_cost = herb_dto.cost * amount

        if total_cost <= self._mana:
            self._mana -= total_cost

        else:
            raise ValueError("소지금이 부족합니다.")

    def sell_animal(self, name: str, level: int, amount: int):
        animal_dto = self._animals.get(name)[level - 1]

        if animal_dto.amount >= amount:
            animal_dto.amount -= amount
            self._mana += animal_dto.sell_cost * amount

        else:
            raise ValueError("해당 마법 동물을 소유하고 있지 않거나 수가 부족합니다.")

    def buy_animal(self, name: str, level: int, amount: int):
        animal_dto = self._animals.get(name)[level - 1]
        total_cost = animal_dto.buy_cost * amount

        if self._mana >= total_cost:
            self._mana -= total_cost
            animal_dto.amount += amount

        else:
            raise ValueError("소지금이 부족합니다.")

    def train_animal(self, name: str, level: int, amount: int):
        # self._animals.get(<animal name>)의 인덱스는 1~3레벨이 각각 0~2에 해당함
        # 이 함수를 사용전에 level값으로 들어오는 값이 0 ~ 1의 값만 들어올수 있도록 강제해야함
        animal_dto = self._animals.get(name)[level - 1]
        trained_animal_dto = self._animals.get(name)[level]
        total_train_cost = trained_animal_dto.buy_cost * amount

        if animal_dto.amount >= amount and self._mana >= total_train_cost:
            animal_dto.amount -= amount
            trained_animal_dto += amount

            self._mana -= total_train_cost

        else:
            raise ValueError("훈련시킬 대상의 동물의 수가 부족하거나 훈련 비용이 부족합니다.")

    def buy_tool_piece(self, name: str, amount: int):
        tool_dto = self._tools.get(name)
        total_cost = tool_dto.piece_cost * amount

        if self._mana >= total_cost:
            self._mana -= total_cost
            tool_dto.piece += amount

        else:
            raise ValueError("소지금이 부족합니다.")

    def activate_tool(self, name: str):
        tool_dto = self._tools.get(name)

        if tool_dto.piece >= tool_dto.need_piece and self._mana >= tool_dto.craft_cost:
            self._mana -= tool_dto.craft_cost
            tool_dto.activate()

        else:
            raise ValueError("마법 도구 합성에 필요한 조각이 부족하거나 합성 비용이 부족합니다.")

    def use_drugs(self, amount: int):
        if 3000 - (self._drugs + amount) >= 0:
            self._drugs += amount
            self._mana += amount

        else:
            raise ValueError("더이상 마법 약물을 복용할 수 없습니다.")

    def use_medicine(self, amount: int):
        if self._drugs - amount >= 0:
            self._drugs -= amount
            self._mana -= amount

        else:
            raise ValueError("마법 약물을 사용한 이상으로 회복 약물을 복용할 수 없습니다.")

    def get_drugs_debuff(self) -> int:
        return self._drugs // 10

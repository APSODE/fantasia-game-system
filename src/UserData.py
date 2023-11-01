from typing import Optional, List, Dict
from src.MagicalToolData import MagicalToolData
from src.MagicalAnimalData import MagicalAnimalData
from src.MagicalHerbData import MagicalHerbData
from FantasiaSetting import HERB_COST_DATA, ANIMAL_COST_DATA, TOOL_COST_DATA


class UserData:
    def __init__(self,
                 color: str,
                 mana: int,
                 ):

        self._color = color
        self._mana = mana
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

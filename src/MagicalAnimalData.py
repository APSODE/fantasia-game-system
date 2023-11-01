from typing import Optional, Dict


class MagicalAnimalData:
    def __init__(self,
                 name: str,
                 round: int,
                 buy_cost_data: Dict[str, int],
                 sell_cost_data: Dict[str, int],
                 profit_data: Dict[str, int],
                 level: int = 1
                 ):

        self._name = name
        self._round = round
        self._level = level
        self._buy_cost_data = buy_cost_data
        self._sell_cost_data = sell_cost_data
        self._profit_data = profit_data

    @property
    def name(self) -> str:
        return self._name

    @property
    def buy_cost(self) -> Optional[int]:
        return self._buy_cost_data.get(f"{self._level}")

    @property
    def sell_cost(self) -> Optional[int]:
        return self._sell_cost_data.get(f"{self._level}")
    
    # @property
    # def (self):
    #     return




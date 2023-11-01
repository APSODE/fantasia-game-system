from typing import Optional, Dict


class MagicalAnimalData:
    def __init__(self,
                 name: str,
                 round: int,
                 level: int,
                 buy_cost_data: Dict[str, int],
                 sell_cost_data: Dict[str, int],
                 profit_data: Dict[str, int]):

        self._name = name
        self._round = round
        self._level = level
        self._buy_cost_data = buy_cost_data
        self._sell_cost_data = sell_cost_data
        self._profit_data = profit_data

    @staticmethod
    def create_object(name: str,
                      round: int,
                      buy_cost_data: Dict[str, int],
                      sell_cost_data: Dict[str, int],
                      profit_data: Dict[str, int],
                      level: int = 1) -> "MagicalAnimalData":

        return MagicalAnimalData(
            name = name,
            round = round,
            buy_cost_data = buy_cost_data,
            sell_cost_data = sell_cost_data,
            profit_data = profit_data,
            level = level
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def buy_cost(self) -> Optional[int]:
        """현재 레벨에 대한 구매 비용"""
        return self._buy_cost_data.get(f"{self._level}")

    @property
    def sell_cost(self) -> Optional[int]:
        """현재 레벨에 대한 판매 수익"""
        return self._sell_cost_data.get(f"{self._level}")

    @property
    def profit(self) -> Optional[int]:
        """현재 레벨에 대한 월 수익"""
        return self._profit_data.get(f"{self._level}")



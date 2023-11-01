from typing import Optional, Dict, List


class MagicalAnimalData:
    def __init__(self, buy_cost: int, sell_cost: int, profit: int):
        self._buy_cost = buy_cost
        self._sell_cost = sell_cost
        self._profit = profit

    @staticmethod
    def create_object(buy_cost: int, sell_cost: int, profit: int):
        return MagicalAnimalData(
            buy_cost = buy_cost,
            sell_cost = sell_cost,
            profit = profit
        )

    @staticmethod
    def create_initial_value(animal_cost_data: Dict[str, Dict[str, int]]) -> List["MagicalAnimalData"]:
        temp = []

        for level in range(1, 4):
            temp.append(
                MagicalAnimalData.create_object(
                    buy_cost = animal_cost_data.get("buy").get(f"{level}"),
                    sell_cost = animal_cost_data.get("sell").get(f"{level}"),
                    profit = animal_cost_data.get("profit").get(f"{level}")
                )
            )

        return temp

    @property
    def buy_cost(self) -> int:
        return self._buy_cost

    @buy_cost.setter
    def buy_cost(self, value: int):
        self._buy_cost = value

    @property
    def sell_cost(self) -> int:
        return self._sell_cost

    @sell_cost.setter
    def sell_cost(self, value: int):
        self._sell_cost = value

    @property
    def profit(self) -> int:
        return self._profit

    @profit.setter
    def profit(self, value: int):
        self._profit = value


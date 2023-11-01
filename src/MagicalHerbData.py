from typing import Optional, Dict, List


class MagicalHerbData:
    def __init__(self, round: int, amount: int, cost_data: Dict[str, int]):
        self._round = round
        self._amount = amount
        self._cost_data = cost_data

    @staticmethod
    def create_object(cost_data: Dict[str, int], amount: int = 0, round: int = 1) -> "MagicalHerbData":
        return MagicalHerbData(
            round = round,
            amount = amount,
            cost_data = cost_data
        )

    @staticmethod
    def create_initial_value(cost_data: Dict[str, int]) -> "MagicalHerbData":
        return MagicalHerbData.create_object(cost_data = cost_data)

    @property
    def round(self) -> int:
        return self._round

    @round.setter
    def round(self, value: int):
        self._round = value

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int):
        self._amount = value

    @property
    def cost(self) -> int:
        """현재 라운드 기준 구매/판매 비용"""
        return self._cost_data.get(f"{self._round}")
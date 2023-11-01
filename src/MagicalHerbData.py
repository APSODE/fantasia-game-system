from typing import Optional, Dict


class MagicalHerbData:
    def __init__(self, name: str, round: int, cost_data: Dict[str, int]):
        self._name = name
        self._round = round
        self._cost_data = cost_data

    @staticmethod
    def create_object(name: str, round: int, cost_data: Dict[str, int]) -> "MagicalHerbData":
        return MagicalHerbData(
            name = name,
            round = round,
            cost_data = cost_data
        )

    @property
    def name(self):
        return self._name

    @property
    def round(self):
        return self._round

    @property
    def cost(self):
        """현재 라운드 기준 구매/판매 비용"""
        return self._cost_data.get(f"{self._round}")
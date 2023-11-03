from typing import Optional, Dict, List


class MagicalToolData:
    def __init__(self,
                 piece: int,
                 need_piece: int,
                 piece_cost: int,
                 craft_cost: int,
                 profit: int):

        self._piece = piece
        self._need_piece = need_piece
        self._piece_cost = piece_cost
        self._craft_cost = craft_cost
        self._profit = profit
        self._purchaseable = False
        self._is_activated = False

    @staticmethod
    def create_object(need_piece: int,
                      piece_cost: int,
                      craft_cost: int,
                      profit: int,
                      piece: int = 0) -> "MagicalToolData":

        return MagicalToolData(
            piece = piece,
            need_piece = need_piece,
            piece_cost = piece_cost,
            craft_cost = craft_cost,
            profit = profit
        )

    @property
    def piece(self) -> int:
        return self._piece

    @piece.setter
    def piece(self, value: int):
        self._piece = value

    @property
    def need_piece(self) -> int:
        return self._need_piece

    @property
    def piece_cost(self) -> int:
        return self._piece_cost

    @property
    def craft_cost(self) -> int:
        return self._craft_cost

    @property
    def profit(self) -> int:
        return self._profit

    @property
    def is_activated(self) -> bool:
        return self._is_activated

    def add_piece(self, amount: int):
        self._piece += amount

    def activate(self):
        self._is_activated = True

    def purchaseable(self):
        self._purchaseable = True




# # 마법도구 데이터 정의
# magical_tools = {
#     "마법부적": MagicalToolsData("마법부적", 1, 1, {"1": 300}, {"1": 1000}, {"1": 700}),
#     "마법지도": MagicalToolsData("마법지도", 1, 1, {"1": 500}, {"1": 1500}, {"1": 1000}),
#     "마법양초": MagicalToolsData("마법양초", 1, 1, {"1": 500}, {"1": 1800}, {"1": 1300}),
#     "마법거울": MagicalToolsData("마법거울", 1, 1, {"1": 2000}, {"1": 5000}, {"1": 3000}),
#     "지팡이": MagicalToolsData("지팡이", 1, 1, {"1": 4000}, {"1": 8000}, {"1": 4000}),
#     "빗자루": MagicalToolsData("빗자루", 1, 1, {"1": 4000}, {"1": 9500}, {"1": 5500}),
# }
#
# # 예제로 특정 마법도구 데이터 출력
# magical_tool = magical_tools["마법부적"]
# print(f"도구 이름: {magical_tool.name}")
# print(f"도구 Piece: {magical_tool.piece}")
# print(f"구매 비용: {magical_tool.buy_cost}")
# print(f"판매 비용: {magical_tool.sell_cost}")
# print(f"이익: {magical_tool.profit}")

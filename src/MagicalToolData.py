from typing import Optional, Dict

class MagicalToolsData:
    def __init__(self, name: str, round: int, piece: int, buy_cost_data: Dict[str, int], sell_cost_data: Dict[str, int], profit_data: Dict[str, int]):

        self._name = name
        self._round = round
        self._piece = piece
        self._buy_cost_data = buy_cost_data
        self._sell_cost_data = sell_cost_data
        self._profit_data = profit_data

    @staticmethod
    def create_object(name: str,
                      round: int,
                      buy_cost_data: Dict[str, int],
                      sell_cost_data: Dict[str, int],
                      profit_data: Dict[str, int],
                      piece: int = 1) -> "MagicalToolsData":
        return MagicalToolsData(
            name=name,
            round=round,
            buy_cost_data=buy_cost_data,
            sell_cost_data=sell_cost_data,
            profit_data=profit_data,
            piece=piece
        )

    @property
    def name(self) -> str:
        return self._name

    @property
    def round(self) -> int:
        return self._round

    @property
    def piece(self) -> int:
        return self._piece

    @property
    def buy_cost(self) -> Optional[int]:
        return self._buy_cost_data.get(str(self._piece))

    @property
    def sell_cost(self) -> Optional[int]:
        return self._sell_cost_data.get(str(self._piece))

    @property
    def profit(self) -> Optional[int]:
        return self._profit_data.get(str(self._piece))

# 마법도구 데이터 정의
magical_tools = {
    "마법부적": MagicalToolsData("마법부적", 1, 1, {"1": 300}, {"1": 1000}, {"1": 700}),
    "마법지도": MagicalToolsData("마법지도", 1, 1, {"1": 500}, {"1": 1500}, {"1": 1000}),
    "마법양초": MagicalToolsData("마법양초", 1, 1, {"1": 500}, {"1": 1800}, {"1": 1300}),
    "마법거울": MagicalToolsData("마법거울", 1, 1, {"1": 2000}, {"1": 5000}, {"1": 3000}),
    "지팡이": MagicalToolsData("지팡이", 1, 1, {"1": 4000}, {"1": 8000}, {"1": 4000}),
    "빗자루": MagicalToolsData("빗자루", 1, 1, {"1": 4000}, {"1": 9500}, {"1": 5500}),
}

# 예제로 특정 마법도구 데이터 출력
magical_tool = magical_tools["마법부적"]
print(f"도구 이름: {magical_tool.name}")
print(f"도구 Piece: {magical_tool.piece}")
print(f"구매 비용: {magical_tool.buy_cost}")
print(f"판매 비용: {magical_tool.sell_cost}")
print(f"이익: {magical_tool.profit}")

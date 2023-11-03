#================== 해당 데이터들은 실시간 반영이 아닌 상수임 ==================#
#================== 절대 변경하지마 절대 변경하지마 절대 변경하지마  ==================#
HERB_COST_DATA = {
    # round 별로 금액 지정
    "캐오닌": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
    "바카스": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
    "코로롱": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
    "버들": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
    "번개": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
    "버프": {
        "1": 100,
        "2": 200,
        "3": 300,
        "4": 400,
        "5": 500,
        "6": 600,
        "7": 700,
        "8": 800,
        "9": 900
    },
}

ANIMAL_COST_DATA = {
    "퍼프": {
        "buy": {
            "1": 200,
            "2": 800,
            "3": 2000
        },
        "sell": {
            "1": 3000,
            "2": 5500,
            "3": 7500
        },
        "profit": {
            "1": 12,
            "2": 32,
            "3": 80
        }
    },
    "주디": {
        "buy": {
            "1": 300,
            "2": 700,
            "3": 2500
        },
        "sell": {
            "1": 3000,
            "2": 5000,
            "3": 8200
        },
        "profit": {
            "1": 10,
            "2": 30,
            "3": 100
        }
    },
    "위즈": {
        "buy": {
            "1": 400,
            "2": 1200,
            "3": 3200
        },
        "sell": {
            "1": 3500,
            "2": 6000,
            "3": 9000
        },
        "profit": {
            "1": 13,
            "2": 14,
            "3": 200
        }
    },
    "주비": {
        "buy": {
            "1": 400,
            "2": 700,
            "3": 3000
        },
        "sell": {
            "1": 3500,
            "2": 5000,
            "3": 8700
        },
        "profit": {
            "1": 14,
            "2": 40,
            "3": 170
        }
    },
    "유니콘": {
        "buy": {
            "1": 500,
            "2": 1200,
            "3": 4000
        },
        "sell": {
            "1": 4000,
            "2": 6500,
            "3": 10000
        },
        "profit": {
            "1": 20,
            "2": 40,
            "3": 200
        }
    },
    "불사조": {
        "buy": {
            "1": 500,
            "2": 1500,
            "3": 5000
        },
        "sell": {
            "1": 4000,
            "2": 6500,
            "3": 13500
        },
        "profit": {
            "1": 16,
            "2": 60,
            "3": 300
        }
    }
}

TOOL_COST_DATA = {
    "마법부적": {
        "need_piece": 1,
        "piece_cost": 300,
        "profit": 0,
        "craft_cost": 15
    },
    "마법지도": {
        "need_piece": 1,
        "piece_cost": 500,
        "profit": 0,
        "craft_cost": 25
    },
    "마법양초": {
        "need_piece": 3,
        "piece_cost": 500,
        "profit": 50,
        "craft_cost": 100
    },
    "마법거울": {
        "need_piece": 2,
        "piece_cost": 2000,
        "profit": 150,
        "craft_cost": 300
    },
    "지팡이": {
        "need_piece": 2,
        "piece_cost": 4000,
        "profit": 350,
        "craft_cost": 700
    },
    "빗자루": {
        "need_piece": 4,
        "piece_cost": 4000,
        "profit": 800,
        "craft_cost": 1600
    },
}

DEFAULT_TRADEABLE_ANIMALS = {
    "1": [{"퍼프": 1}, {"퍼프": 1}],
    "2": [{"퍼프": 1}, {"퍼프": 1}],
    "3": [{"퍼프": 1}, {"퍼프": 1}],
    "4": [{"퍼프": 1}, {"퍼프": 1}],
    "5": [{"퍼프": 1}, {"퍼프": 1}],
    "6": [{"퍼프": 1}, {"퍼프": 1}],
    "7": [{"퍼프": 1}, {"퍼프": 1}],
    "8": [{"퍼프": 1}, {"퍼프": 1}],
    "9": [{"퍼프": 1}, {"퍼프": 1}]
}

USER_COLORS = ["RED", "YELLOW", "GREEN", "BLUE", "WHITE", "BLACK"]

USER_CARDS = ["herb", "tool", "animal"]
CARD_NAMES = {
    "herbs": ["캐오닌", "바카스", "코로롱", "버들", "번개", "버프"],
    "animal": ["퍼프", "주디", "주비", "위즈", "유니콘", "불사조"],
    "tool": ["마법부적", "마법지도", "마법양초", "마법거울", "지팡이", "빗자루"]
}

CARD_TAG_TO_KR = {
    "herb": "마법 약초",
    "animal": "마법 동물",
    "tool": "마법 도구"
}

HERB_CARD = "herb"
TOOL_CARD = "tool"
ANIMAL_CARD = "animal"

#================== 절대 변경하지마 절대 변경하지마 절대 변경하지마  ==================#
#================== 해당 데이터들은 실시간 반영이 아닌 상수임 ==================#



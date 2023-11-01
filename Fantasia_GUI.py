import tkinter as tk
from FantasiaSetting import USER_COLORS
from src.UserData import UserData


class FantasiaUI:
    def __init__(self, root=None, user_data=None):

        self.root = root
        if root:
            self.root.title(f"판타지아 게임 - {user_data.color} 유저")

        self.user_data = user_data

        if root:
            self.create_ui()

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.current_round_label = tk.Label(self.main_frame, text=f"현재 라운드: {self.fantasia.round}")
        self.current_round_label.pack()

        self.set_tradeable_animal_button = tk.Button(self.main_frame, text="거래 가능 동물 설정", command=self.set_tradeable_animal)
        self.set_tradeable_animal_button.pack()

        self.init_tradeable_animal_button = tk.Button(self.main_frame, text="거래 가능 동물 초기화", command=self.init_tradeable_animal)
        self.init_tradeable_animal_button.pack()

    def set_tradeable_animal(self):
        animal_name = input("거래 가능 동물 이름을 입력하세요: ")
        animal_level = int(input("동물 레벨을 입력하세요: "))
        self.fantasia.set_tradeable_animal(animal_name, animal_level)

    def init_tradeable_animal(self):
        self.fantasia.init_tradeable_animal()

    def update_round_label(self):
        self.current_round_label.config(text=f"현재 라운드: {self.fantasia.round}")

    def start_game(self):
        self.root.mainloop()

class Fantasia:
    def __init__(self):


    def set_tradeable_animal(self, name, level):
        self._tradeable_animals[name] = level

    def init_tradeable_animal(self):
        self._tradeable_animals.clear()

    @property
    def round(self):
        return self._round

    def __init__(self, root, user_data):
        self.root = root
        self.root.title(f"판타지아 게임 - {user_data.color} 유저")

        self.user_data = user_data

        self.create_ui()

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.mana_label = tk.Label(self.main_frame, text=f"마나: {self.user_data.mana}")
        self.mana_label.pack()

        self.drugs_label = tk.Label(self.main_frame, text=f"마법 약물: {self.user_data.drugs}")
        self.drugs_label.pack()

        self.herb_label = tk.Label(self.main_frame, text="허브:")
        self.herb_label.pack()
        for herb_name, herb_data in self.user_data.herbs.items():
            herb_info = f"{herb_name}: {herb_data.amount}"
            tk.Label(self.main_frame, text=herb_info).pack()

        self.animal_label = tk.Label(self.main_frame, text="마법 동물:")
        self.animal_label.pack()
        for animal_name, animal_data_list in self.user_data.animals.items():
            for level, animal_data in enumerate(animal_data_list, start=1):
                animal_info = f"{animal_name} 레벨 {level}: {animal_data.amount}"
                tk.Label(self.main_frame, text=animal_info).pack()

        self.tool_label = tk.Label(self.main_frame, text="마법 도구:")
        self.tool_label.pack()
        for tool_name, tool_data in self.user_data.tools.items():
            tool_info = f"{tool_name} (조각: {tool_data.piece})"
            tk.Label(self.main_frame, text=tool_info).pack()

        self.sell_herb_button = tk.Button(self.main_frame, text="허브 판매", command=self.sell_herb)
        self.sell_herb_button.pack()

        self.buy_herb_button = tk.Button(self.main_frame, text="허브 구매", command=self.buy_herb)
        self.buy_herb_button.pack()

        self.sell_animal_button = tk.Button(self.main_frame, text="마법 동물 판매", command=self.sell_animal)
        self.sell_animal_button.pack()

        self.buy_animal_button = tk.Button(self.main_frame, text="마법 동물 구매", command=self.buy_animal)
        self.buy_animal_button.pack()

        self.train_animal_button = tk.Button(self.main_frame, text="마법 동물 훈련", command=self.train_animal)
        self.train_animal_button.pack()

        self.buy_tool_piece_button = tk.Button(self.main_frame, text="도구 조각 구매", command=self.buy_tool_piece)
        self.buy_tool_piece_button.pack()

        self.activate_tool_button = tk.Button(self.main_frame, text="도구 활성화", command=self.activate_tool)
        self.activate_tool_button.pack()

        self.use_drugs_button = tk.Button(self.main_frame, text="마법 약물 복용", command=self.use_drugs)
        self.use_drugs_button.pack()

        self.use_medicine_button = tk.Button(self.main_frame, text="회복 약물 복용", command=self.use_medicine)
        self.use_medicine_button.pack()

    def sell_herb(self):
        herb_name = input("판매할 허브 이름을 입력하세요: ")
        herb_amount = int(input("판매할 허브 갯수를 입력하세요: "))
        try:
            self.user_data.sell_herb(herb_name, herb_amount)
            self.update_labels()
        except ValueError as e:
            print(f"판매 실패: {e}")

    def buy_herb(self):
        herb_name = input("구매할 허브 이름을 입력하세요: ")
        herb_amount = int(input("구매할 허브 갯수를 입력하세요: "))
        try:
            self.user_data.buy_herb(herb_name, herb_amount)
            self.update_labels()
        except ValueError as e:
            print(f"구매 실패: {e}")

    def sell_animal(self):
        animal_name = input("판매할 마법 동물 이름을 입력하세요: ")
        animal_level = int(input("동물 레벨을 입력하세요: "))
        animal_amount = int(input("판매할 마법 동물 갯수를 입력하세요: "))
        try:
            self.user_data.sell_animal(animal_name, animal_level, animal_amount)
            self.update_labels()
        except ValueError as e:
            print(f"판매 실패: {e}")

    def buy_animal(self):
        animal_name = input("구매할 마법 동물 이름을 입력하세요: ")
        animal_level = int(input("동물 레벨을 입력하세요: "))
        animal_amount = int(input("구매할 마법 동물 갯수를 입력하세요: "))
        try:
            self.user_data.buy_animal(animal_name, animal_level, animal_amount)
            self.update_labels()
        except ValueError as e:
            print(f"구매 실패: {e}")

    def train_animal(self):
        animal_name = input("훈련할 마법 동물 이름을 입력하세요: ")
        animal_level = int(input("동물 레벨을 입력하세요: "))
        train_amount = int(input("훈련할 마법 동물 갯수를 입력하세요: "))
        try:
            self.user_data.train_animal(animal_name, animal_level, train_amount)
            self.update_labels()
        except ValueError as e:
            print(f"훈련 실패: {e}")

    def buy_tool_piece(self):
        tool_name = input("구매할 도구 조각 이름을 입력하세요: ")
        piece_amount = int(input("구매할 도구 조각 갯수를 입력하세요: "))
        try:
            self.user_data.buy_tool_piece(tool_name, piece_amount)
            self.update_labels()
        except ValueError as e:
            print(f"구매 실패: {e}")

    def activate_tool(self):
        tool_name = input("활성화할 도구 이름을 입력하세요: ")
        try:
            self.user_data.activate_tool(tool_name)
            self.update_labels()
        except ValueError as e:
            print(f"활성화 실패: {e}")

    def use_drugs(self):
        drugs_amount = int(input("복용할 마법 약물 갯수를 입력하세요: "))
        try:
            self.user_data.use_drugs(drugs_amount)
            self.update_labels()
        except ValueError as e:
            print(f"복용 실패: {e}")

    def use_medicine(self):
        medicine_amount = int(input("복용할 회복 약물 갯수를 입력하세요: "))
        try:
            self.user_data.use_medicine(medicine_amount)
            self.update_labels()
        except ValueError as e:
            print(f"복용 실패: {e}")

    def update_labels(self):
        self.mana_label.config(text=f"마나: {self.user_data.mana}")
        self.drugs_label.config(text=f"마법 약물: {self.user_data.drugs}")
        for herb_name, herb_data in self.user_data.herbs.items():
            herb_info = f"{herb_name}: {herb_data.amount}"
            # Find the label widget by its text and update the text value
            for label in self.main_frame.winfo_children():
                if label["text"] == herb_info:
                    label.config(text=herb_info)
        for animal_name, animal_data_list in self.user_data.animals.items():
            for level, animal_data in enumerate(animal_data_list, start=1):
                animal_info = f"{animal_name} 레벨 {level}: {animal_data.amount}"
                for label in self.main_frame.winfo_children():
                    if label["text"] == animal_info:
                        label.config(text=animal_info)
        for tool_name, tool_data in self.user_data.tools.items():
            tool_info = f"{tool_name} (조각: {tool_data.piece})"
            for label in self.main_frame.winfo_children():
                if label["text"] == tool_info:
                    label.config(text=tool_info)

if __name__ == "__main__":
    root = tk.Tk()
    fantasia_ui = FantasiaUI(root)
    fantasia_ui.start_game()

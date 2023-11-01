import tkinter as tk
from tkinter import Tk
from Fantasia import Fantasia

class FantasiaUI:
    def __init__(self, root: Tk):
        self.root = root
        self.fantasia = Fantasia()  # Fantasia 인스턴스를 초기화합니다
        self.user_color = "RED"  # 기본 설정값
        self.user_data = self.fantasia.get_user(self.user_color)  # 기본 설정값
        self.root.title(f"판타지아 게임 - {self.user_data.color} 유저")
        self.create_ui()
        self.fantasia.set_tradeable_animal("퍼프", 1)

    def create_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.mana_label = tk.Label(self.main_frame, text="")
        self.mana_label.pack()

        self.drugs_label = tk.Label(self.main_frame, text="")
        self.drugs_label.pack()

        self.herb_label = tk.Label(self.main_frame, text="허브:")
        self.herb_label.pack()

        self.animal_label = tk.Label(self.main_frame, text="마법 동물:")
        self.animal_label.pack()

        self.tool_label = tk.Label(self.main_frame, text="마법 도구:")
        self.tool_label.pack()

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

    def update_labels(self):
        self.mana_label.config(text=f"마나: {self.user_data.mana}")
        self.drugs_label.config(text=f"마법 약물: {self.user_data.drugs}")

        # "허브" 레이블 아래에 변수 허브 정보 표시
        herb_info = "\n".join([f"{herb_name}: {herb_data.amount}" for herb_name, herb_data in self.user_data.herbs.items()])
        self.herb_label.config(text=f"허브:\n{herb_info}")

        # "마법 동물" 레이블 아래에 변수 마법 동물 정보 표시
        animal_info = ""
        for animal_name, animal_data_list in self.user_data.animals.items():
            for level, animal_data in enumerate(animal_data_list, start=1):
                animal_info += f"{animal_name} 레벨 {level}: {animal_data.amount}\n"
        self.animal_label.config(text=f"마법 동물:\n{animal_info}")

        # "마법 도구" 레이블 아래에 변수 마법 도구 정보 표시
        tool_info = "\n".join([f"{tool_name} (조각: {tool_data.piece})" for tool_name, tool_data in self.user_data.tools.items()])
        self.tool_label.config(text=f"마법 도구:\n{tool_info}")

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


if __name__ == "__main__":
    root = tk.Tk()
    fantasia_ui = FantasiaUI(root)
    fantasia_ui.root.mainloop()



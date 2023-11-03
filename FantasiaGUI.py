from typing import Optional, Dict, Literal, Callable, List
from tkinter import Tk, Frame, LabelFrame, Button, Widget, OptionMenu, StringVar, Label, simpledialog, messagebox, \
    Toplevel, Entry, Radiobutton, IntVar
from tkinter.ttk import Combobox

from Fantasia import Fantasia
from FantasiaSetting import USER_COLORS, USER_CARDS, CARD_NAMES, CARD_TAG_TO_KR
from src.MagicalToolData import MagicalToolData


class _ComponentContainer:
    def __init__(self):
        self._frame: Dict[str, Frame] = {}
        self._label_frame: Dict[str, LabelFrame] = {}
        self._button: Dict[str, Button] = {}
        self._combobox: Dict[str, Combobox] = {}
        self._option_menu: Dict[str, OptionMenu] = {}
        self._string_var: Dict[str, StringVar] = {}
        self._label: Dict[str, Label] = {}
        self._entry: Dict[str, Entry] = {}
        self._radio_button: Dict[str, Radiobutton] = {}
        self._integer_var: Dict[str, IntVar] = {}

    @property
    def frame(self) -> Dict[str, Frame]:
        return self._frame

    @frame.setter
    def frame(self, value: Dict[str, Frame]):
        self._frame = value

    @property
    def label_frame(self) -> Dict[str, LabelFrame]:
        return self._label_frame

    @label_frame.setter
    def label_frame(self, value: Dict[str, LabelFrame]):
        self._label_frame = value

    @property
    def button(self) -> Dict[str, Button]:
        return self._button

    @button.setter
    def button(self, value: Dict[str, Button]):
        self._button = value

    @property
    def combobox(self) -> Dict[str, Combobox]:
        return self._combobox

    @combobox.setter
    def combobox(self, value: Dict[str, Combobox]):
        self._combobox = value

    @property
    def option_menu(self) -> Dict[str, OptionMenu]:
        return self._option_menu

    @option_menu.setter
    def option_menu(self, value: Dict[str, OptionMenu]):
        self._option_menu = value

    @property
    def string_var(self) -> Dict[str, StringVar]:
        return self._string_var

    @string_var.setter
    def string_var(self, value: Dict[str, StringVar]):
        self._string_var = value

    @property
    def integer_var(self) -> Dict[str, IntVar]:
        return self._integer_var

    @integer_var.setter
    def integer_var(self, value: Dict[str, IntVar]):
        self._integer_var = value

    @property
    def label(self) -> Dict[str, Label]:
        return self._label

    @label.setter
    def label(self, value: Dict[str, Label]):
        self._label = value

    @property
    def entry(self) -> Dict[str, Entry]:
        return self._entry

    @entry.setter
    def entry(self, value: Dict[str, Entry]):
        self._entry = value

    @property
    def radio_button(self) -> Dict[str, Radiobutton]:
        return self._radio_button

    @radio_button.setter
    def radio_button(self, value: Dict[str, Radiobutton]):
        self._radio_button = value

    def get_frame(self, name: str) -> Frame:
        return self._frame.get(name)

    def get_label_frame(self, name: str) -> LabelFrame:
        return self._label_frame.get(name)

    def get_string_var(self, name: str) -> StringVar:
        return self._string_var.get(name)

    def get_integer_var(self, name: str) -> IntVar:
        return self._integer_var.get(name)

    def get_option_menu(self, name: str) -> OptionMenu:
        return self._option_menu.get(name)

    def get_button(self, name: str) -> Button:
        return self._button.get(name)

    def get_entry(self, name: str) -> Entry:
        return self._entry.get(name)

    def get_label(self, name: str) -> Label:
        return self._label.get(name)

    def get_radio_button(self, name: str) -> Radiobutton:
        return self._radio_button.get(name)

    def set_string_var_value(self, name: str, value: str):
        self._string_var.get(name).set(value)

    def set_integer_var_value(self, name: str, value: int):
        self._integer_var.get(name).set(value)

    def add_label_frame(self, name: str, widget: LabelFrame):
        self._label_frame.update({name: widget})

    def add_frame(self, name: str, widget: Frame):
        self._frame.update({name: widget})

    def add_button(self, name: str, widget: Button):
        self._button.update({name: widget})

    def add_combobox(self, name: str, widget: Combobox):
        self._combobox.update({name: widget})

    def add_option_menu(self, name: str, widget: OptionMenu):
        self._option_menu.update({name: widget})

    def add_string_var(self, name: str):
        self._string_var.update({name: StringVar()})

    def add_integet_var(self, name: str):
        self._integer_var.update({name: IntVar()})

    def add_label(self, name: str, widget: Label):
        self._label.update({name: widget})

    def add_entry(self, name: str, widget: Entry):
        self._entry.update({name: widget})

    def add_radio_button(self, name: str, widget: Radiobutton):
        self._radio_button.update({name: widget})


class TradeableAnimalsController(Toplevel):
    def __init__(self, master: Tk, fantasia_instance: Fantasia):
        super().__init__(master = master)
        self._fantasia = fantasia_instance
        self._components = _ComponentContainer()
        self._set_var()
        self._set_initial_window()
        self._render_component()

    def _set_var(self):
        for seperator in ["f", "s"]:
            for num in range(1, 10):
                self._components.add_string_var(f"round_{num}_{seperator}_animal_name")
                self._components.set_string_var_value(f"round_{num}_{seperator}_animal_name", "퍼프")
                self._components.add_string_var(f"round_{num}_{seperator}_animal_level")
                self._components.set_string_var_value(f"round_{num}_{seperator}_animal_level", "1")

    def _set_initial_window(self):
        center_x = (self.winfo_screenwidth() // 2) - 330
        center_y = (self.winfo_screenheight() // 2) - 450
        self.geometry(f"660x900+{center_x}+{center_y}")
        # self.resizable(False, False)
        # self.minsize(400, 800)
        # self.maxsize(400, 800)

    def _render_component(self):
        self._set_frame()
        self._set_label_frame()
        self._set_option_menu()
        self._set_button()

    def _set_frame(self):
        f_animal_frame = Frame(self)
        f_animal_frame.grid(row = 0, column = 0)
        self._components.add_frame("f_animal_frame", f_animal_frame)

        s_animal_frame = Frame(self)
        s_animal_frame.grid(row = 0, column = 1)
        self._components.add_frame("s_animal_frame", s_animal_frame)

        save_button_frame = Frame(self)
        save_button_frame.grid(row = 0, column = 2)
        self._components.add_frame("save_btn_frame", save_button_frame)

    def _set_label_frame(self):
        for seperator in ["f", "s"]:
            for round in range(1, 10):
                round_label_frame = LabelFrame(
                    self._components.get_frame(f"{seperator}_animal_frame"),
                    text = f"{round}라운드 판매 가능 마법 동물"
                )

                name_label_frame = LabelFrame(
                    round_label_frame,
                    text = "마법 동물"
                )

                level_label_frame = LabelFrame(
                    round_label_frame,
                    text = "레벨"
                )
                round_label_frame.pack(side = "top", anchor = "center")
                name_label_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
                level_label_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
                self._components.add_label_frame(f"round_{round}_{seperator}_animal", round_label_frame)
                self._components.add_label_frame(f"round_{round}_{seperator}_animal_name", name_label_frame)
                self._components.add_label_frame(f"round_{round}_{seperator}_animal_level", level_label_frame)

    def _set_option_menu(self):
        for seperator in ["f", "s"]:
            for round in range(1, 10):
                name_round_label_frame = self._components.get_label_frame(f"round_{round}_{seperator}_animal_name")
                level_round_label_frame = self._components.get_label_frame(f"round_{round}_{seperator}_animal_level")

                round_animal_name_option_menu = OptionMenu(
                    name_round_label_frame,
                    self._components.get_string_var(f"round_{round}_{seperator}_animal_name"),
                    "퍼프",
                    *CARD_NAMES.get("animal")[1:]
                )
                round_animal_name_option_menu.pack(anchor = "center", padx = 30, pady = 10)
                self._components.add_option_menu(
                    f"round_{round}_{seperator}_animal_name",
                    round_animal_name_option_menu
                )

                round_animal_level_option_menu = OptionMenu(
                    level_round_label_frame,
                    self._components.get_string_var(f"round_{round}_{seperator}_animal_level"),
                    "1",
                    *["2", "3"]
                )
                round_animal_level_option_menu.pack(anchor = "center", padx = 30, pady = 10)
                self._components.add_option_menu(
                    f"round_{round}_{seperator}_animal_level",
                    round_animal_level_option_menu
                )

    def _set_button(self):
        save_button = Button(
            self._components.get_frame("save_btn_frame"),
            text = "확인",
            width = 6,
            height = 2,
            command = self._set_tradeable_animals
        )
        save_button.pack(anchor = "center", padx = 30)
        self._components.add_button("save_button", save_button)

    def _set_tradeable_animals(self):
        for round in range(1, 10):
            round_animal_datas = []
            for seperator in ["f", "s"]:
                round_animal_name_var = self._components.get_string_var(f"round_{round}_{seperator}_animal_name")
                round_animal_level_var = self._components.get_string_var(f"round_{round}_{seperator}_animal_level")

                round_animal_datas.append({
                        round_animal_name_var.get(): round_animal_level_var.get()
                })

            self._fantasia.tradeable_animals.update({f"{round}": round_animal_datas})

        self.destroy()


class AdminController(Toplevel):
    def __init__(self, master: Tk, fantasia_instance: Fantasia):
        super().__init__(master = master)
        self._fantasia = fantasia_instance
        self._components = _ComponentContainer()
        self._set_initial_window()
        self._set_var()
        self._render_component()

    def _set_initial_window(self):
        center_x = (self.winfo_screenwidth() // 2) - 350
        center_y = (self.winfo_screenheight() // 2) - 310
        self.title("Fantasia v1.0 - Admin Controller")
        self.geometry(f"700x620+{center_x}+{center_y}")
        # self.resizable(False, False)

    def _render_component(self):
        self._set_frame()
        self._set_label_frame()
        self._set_label()
        self._set_option_menu()
        self._set_button()
        self._set_entry()
        self._set_radio_button()

    def _set_var(self):
        self._components.add_string_var("select_user")
        self._components.set_string_var_value("select_user", "RED")
        self._components.add_string_var("user_card")
        self._components.set_string_var_value("user_card", "herbs")
        self._components.add_string_var("card_name")
        self._components.set_string_var_value("card_name", "없음")
        self._components.add_string_var("card_level")
        self._components.set_string_var_value("card_level", "1")
        self._components.add_integet_var("mana_or_etc")
        self._components.set_integer_var_value("mana_or_etc", 1)

        self._set_var_tracer()

    def _set_var_tracer(self):
        self._components.get_string_var("select_user").trace_add(
            mode = "write",
            callback = self._update_user_data_label
        )
        self._components.get_string_var("user_card").trace_add(
            mode="write",
            callback=self._update_card_names
        )

    def _set_frame(self):
        data_frame = Frame(self)
        data_frame.pack(side = "top", anchor = "center", pady = 5)

        select_frame = Frame(self)
        select_frame.pack(side = "top", anchor = "center", padx = 15, pady = 5)

        button_and_input_frame = Frame(self)
        button_and_input_frame.pack(side = "top", anchor = "center", padx = 15, pady = 5)

        button_frame = Frame(button_and_input_frame)
        button_frame.grid(row = 0, column = 1, padx = 15, pady = 5)

        input_frame = Frame(button_and_input_frame)
        input_frame.grid(row = 0, column = 0, padx = 15, pady = 5)

        self._components.add_frame("data_frame", data_frame)
        self._components.add_frame("select_frame", select_frame)
        self._components.add_frame("button_frame", button_frame)
        self._components.add_frame("input_frame", input_frame)

    def _set_label_frame(self):
        self._set_user_data_label_frame()

        sf_internal_label_frame = LabelFrame(
            self._components.get_frame("select_frame"),
            text = "유저 설정 및 수정 데이터 지정"
        )
        sf_internal_label_frame.pack(padx = 25, pady = 25)
        self._components.add_label_frame("sf_internal_label_frame", sf_internal_label_frame)

        edit_target_data_select_label_frame = LabelFrame(
            sf_internal_label_frame,
            text = "수정 데이터 지정"
        )
        edit_target_data_select_label_frame.grid(row = 0, column = 0, pady = 5, padx = 10)
        self._components.add_label_frame("select_target_data", edit_target_data_select_label_frame)

        select_user = LabelFrame(
            sf_internal_label_frame,
            text = "참가자 선택",
        )
        select_user.grid(row = 0, column = 1, pady = 5, padx = 10)
        self._components.add_label_frame("select_user", select_user)

        select_card = LabelFrame(
            sf_internal_label_frame,
            text = "카드 종류 선택"
        )
        select_card.grid(row = 0, column = 2, pady = 5, padx = 10)
        self._components.add_label_frame("user_card", select_card)

        card_name = LabelFrame(
            sf_internal_label_frame,
            text = "카드 이름 선택"
        )
        card_name.grid(row = 0, column = 3, pady = 5, padx = 10)
        self._components.add_label_frame("card_name", card_name)

        card_level = LabelFrame(
            sf_internal_label_frame,
            text = "카드 레벨 선택"
        )
        card_level.grid(row = 0, column = 4, pady = 5, padx = 10)
        self._components.add_label_frame("card_level", card_level)

    def _set_label(self):
        self._set_user_data_label()

    def _set_user_data_label_frame(self):
        herb_data_label_frame = LabelFrame(
            self._components.get_frame("data_frame"),
            text = "마법 약초 현황"
        )
        herb_data_label_frame.grid(row = 0, column = 0)
        self._components.add_label_frame("herb_data_label_frame", herb_data_label_frame)

        animal_data_label_frame = LabelFrame(
            self._components.get_frame("data_frame"),
            text = "마법 동물 현황"
        )
        animal_data_label_frame.grid(row = 0, column = 1)
        self._components.add_label_frame("animal_data_label_frame", animal_data_label_frame)

        tool_data_label_frame = LabelFrame(
            self._components.get_frame("data_frame"),
            text = "마법 도구 현황"
        )
        tool_data_label_frame.grid(row = 0, column = 2)
        self._components.add_label_frame("tool_data_label_frame", tool_data_label_frame)

        user_label_frame = LabelFrame(
            self._components.get_frame("data_frame"),
            text = "유저 정보"
        )
        user_label_frame.grid(row = 1, column = 1, padx = 5, pady = 5)
        self._components.add_label_frame("user_label", user_label_frame)

    def _set_user_data_label(self):
        current_user_data = self._fantasia.get_user(self._get_select_user())

        for idx, herb_name in enumerate(current_user_data.herbs):
            herb_data = current_user_data.herbs.get(herb_name)
            herb_data_string = f"{herb_name} : {herb_data.amount}"
            herb_label = Label(
                self._components.get_label_frame("herb_data_label_frame"),
                text = herb_data_string
            )
            herb_label.grid(row = idx, column = 0, padx = 5, pady = 5)
            self._components.add_label(f"{herb_name}_label", herb_label)

        for idx, animal_name in enumerate(current_user_data.animals):
            animal_data = current_user_data.animals.get(animal_name)
            animal_data_string = "".join([f"{animal_name} : LEVEL{i + 1} : {animal_data[i].amount}\n" for i in range(3)])
            animal_label = Label(
                self._components.get_label_frame("animal_data_label_frame"),
                text = animal_data_string
            )
            animal_label.grid(row = idx - 3 if idx >= 3 else idx, column = 1 if idx >= 3 else 0, padx = 5, pady = 5)
            self._components.add_label(f"{animal_name}_label", animal_label)

        for idx, tool_name in enumerate(current_user_data.tools):
            tool_data = current_user_data.tools.get(tool_name)
            tool_data_string = (f"{tool_name} : "
                                f"{tool_data.piece}/{tool_data.need_piece} : "
                                f"{tool_data.profit if tool_data.is_activated else 0}")
            tool_label = Label(
                self._components.get_label_frame("tool_data_label_frame"),
                text = tool_data_string
            )
            tool_label.grid(row = idx, column = 0, padx = 5, pady = 5)
            self._components.add_label(f"{tool_name}_label", tool_label)

        user_data_string = (f"유저 : {current_user_data.color}\n"
                            f"소유 마나 : {current_user_data.mana}\n"
                            f"다음턴 월급 : {current_user_data.get_current_round_profit()}")

        user_info_label = Label(
            self._components.get_label_frame("user_label"),
            text=user_data_string
        )
        user_info_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self._components.add_label("user_label", user_info_label)

    def _update_user_data_label(self, *args):
        for label_frame_name in ["herb_data_label_frame", "animal_data_label_frame", "tool_data_label_frame"]:
            self._components.get_label_frame(label_frame_name).destroy()

        self._set_user_data_label_frame()
        self._set_user_data_label()

    def _set_option_menu(self):
        user_select_option_menu = OptionMenu(
            self._components.get_label_frame("select_user"),
            self._components.get_string_var("select_user"),
            *USER_COLORS
        )
        user_select_option_menu.grid(row = 0, column = 0, padx = 5, pady = 5)

        user_card_option_menu = OptionMenu(
            self._components.get_label_frame("user_card"),
            self._components.get_string_var("user_card"),
            "herbs",
            *USER_CARDS[1:]
        )
        user_card_option_menu.grid(row = 0, column = 1, padx = 5, pady = 5)
        self._components.add_option_menu("user_card_option_menu", user_card_option_menu)

        card_name_option_menu = OptionMenu(
            self._components.get_label_frame("card_name"),
            self._components.get_string_var("card_name"),
            "없음",
            *CARD_NAMES.get(self._get_user_card())
        )
        card_name_option_menu.grid(row = 0, column = 2, padx = 5, pady = 5)
        self._components.add_option_menu("card_name_option_menu", card_name_option_menu)

        card_level_option_menu = OptionMenu(
            self._components.get_label_frame("card_level"),
            self._components.get_string_var("card_level"),
            "1",
            *["2", "3"]
        )
        card_level_option_menu.grid(row = 0, column = 3, padx = 5, pady = 5)
        self._components.add_option_menu("card_level_option_menu", card_level_option_menu)

    def _update_card_names(self, *args):
        print("업데이트 함수 호출됨")
        card_name_option_menu = self._components.get_option_menu("card_name_option_menu")
        card_name_option_menu.destroy()
        card_name_option_menu = OptionMenu(
            self._components.get_label_frame("card_name"),
            self._components.get_string_var("card_name"),
            "없음",
            *CARD_NAMES.get(self._get_user_card())
        )
        card_name_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("card_name_option_menu", card_name_option_menu)

    def _set_button(self):
        set_button = Button(
            self._components.get_frame("button_frame"),
            text = "변경",
            width = 10,
            height = 2,
            command = lambda: self._edit_user_data(btn_type = "set")
        )
        set_button.grid(row = 0, column = 0, padx = 10, pady = 5)
        self._components.add_button("set_button", set_button)

        add_button = Button(
            self._components.get_frame("button_frame"),
            text = "증가",
            width = 10,
            height = 2,
            command = lambda: self._edit_user_data(btn_type = "add")
        )
        add_button.grid(row = 0, column = 1, padx = 10, pady = 5)
        self._components.add_button("add_button", set_button)

        minus_button = Button(
            self._components.get_frame("button_frame"),
            text = "감소",
            width = 10,
            height = 2,
            command = lambda: self._edit_user_data(btn_type = "minus")
        )
        minus_button.grid(row = 0, column = 2, padx = 10, pady = 5)
        self._components.add_button("minus_button", set_button)

    def _set_entry(self):
        default_string = StringVar()
        default_string.set("0")
        value_input = Entry(
            self._components.get_frame("input_frame"),
            textvariable = default_string
        )
        value_input.pack()
        self._components.add_entry("value_input", value_input)

    def _set_radio_button(self):
        mana = Radiobutton(
            self._components.get_label_frame("select_target_data"),
            text = "마나",
            value = 0,
            variable = self._components.get_integer_var("mana_or_etc"),
            command = self._disable_option_menu
        )
        mana.grid(row = 0, column = 0, padx = 10)
        self._components.add_radio_button("mana", mana)

        not_mana = Radiobutton(
            self._components.get_label_frame("select_target_data"),
            text = "기타",
            value = 1,
            variable = self._components.get_integer_var("mana_or_etc"),
            command = self._enable_option_menu
        )
        not_mana.grid(row = 0, column = 1, padx = 10)
        self._components.add_radio_button("not_mana", not_mana)

    def _enable_option_menu(self):
        user_card = self._components.get_option_menu("user_card_option_menu")
        card_name = self._components.get_option_menu("card_name_option_menu")
        card_level = self._components.get_option_menu("card_level_option_menu")
        user_card.config(state = "normal")
        card_name.config(state = "normal")
        card_level.config(state = "normal")

    def _disable_option_menu(self):
        user_card = self._components.get_option_menu("user_card_option_menu")
        card_name = self._components.get_option_menu("card_name_option_menu")
        card_level = self._components.get_option_menu("card_level_option_menu")
        user_card.config(state = "disabled")
        card_name.config(state = "disabled")
        card_level.config(state = "disabled")

    def _edit_user_data(self, btn_type: Literal["add", "minus", "set"]):
        entry_object = self._components.get_entry("value_input")
        input_value = int(entry_object.get())

        try:
            current_user_data = self._fantasia.get_user(self._get_select_user())
            mana_or_etc = self._components.get_integer_var("mana_or_etc").get()

            if mana_or_etc == 0:
                if btn_type == "add":
                    current_user_data.mana += input_value
                elif btn_type == "minus":
                    current_user_data.mana -= input_value
                elif btn_type == "set":
                    current_user_data.mana = input_value
            else:
                select_user_card = self._get_user_card()
                select_card_name = self._get_user_card_name()
                select_card_level = self._get_card_level()

                op = ""

                if btn_type == "add":
                    op = "+="
                elif btn_type == "minus":
                    op = "-="
                elif btn_type == "set":
                    op = "="

                if select_user_card == "herbs":
                    select_data = current_user_data.herbs.get(select_card_name)
                    if select_data is None:
                        raise ValueError("마법 약초를 지정후 다시 시도하십시오.")

                    if (op == "=" and input_value < 0) or (op == "-=" and select_data.amount - input_value < 0):
                        raise ValueError("해당 마법 약초의 수는 0 이하가 될 수 없습니다.")

                    exec(f"select_data.amount {op} {input_value}")

                elif select_user_card == "animal":
                    select_data = current_user_data.animals.get(select_card_name)
                    if select_data is None:
                        raise ValueError("마법 동물을 지정후 다시 시도하십시오.")

                    if (op == "=" and input_value < 0) or (op == "-=" and select_data[select_card_level - 1].amount - input_value < 0):
                        raise ValueError("해당 마법 동물의 수는 0 이하가 될 수 없습니다.")

                    exec(f"select_data[{select_card_level - 1}].amount {op} {input_value}")

                elif select_user_card == "tool":
                    select_data = current_user_data.tools.get(select_card_name)
                    if select_data is None:
                        raise ValueError("마법 도구를 지정후 다시 시도하십시오.")

                    if op != "-=" and select_data.need_piece - (select_data.piece + input_value) < 0:
                        raise ValueError("최대 소지 가능 갯수를 초과합니다.")

                    if op == "-=" and select_data.piece - input_value < 0:
                        raise ValueError("해당 마법 도구의 조각 갯수는 0 이하가 될 수 없습니다.")

                    exec(f"select_data.piece {op} {input_value}")

            self._update_user_data_label()

        except ValueError as E:
            messagebox.showinfo("에러발생!", E.__str__())

        except Exception as E:
            print(type(E))
            print(E)

    def _get_select_user(self) -> str:
        return self._components.get_string_var("select_user").get()

    def _get_user_card(self) -> str:
        return self._components.get_string_var("user_card").get()

    def _get_user_card_name(self) -> str:
        return self._components.get_string_var("card_name").get()

    def _get_card_level(self) -> int:
        return int(self._components.get_string_var("card_level").get())


class FantasiaGUI(Tk):
    def __init__(self, debug_mode: bool = False):
        super().__init__()
        self._components = _ComponentContainer()
        self._fantasia = Fantasia()
        self._debug_mode = debug_mode
        # OptionMenu객체의 기본값이 보이지 않는 오류가 있음
        # 만약에 고쳐서 사용한다면 고치고 해당 주석을 해제하면 됨
        TradeableAnimalsController(master = self, fantasia_instance = self._fantasia)
        self._set_key_bind()
        self._set_var()
        self._set_initial_window()
        self._render_component()
        self.mainloop()

    @staticmethod
    def grid(widget: Widget, row: int, column: int, **kwargs):
        widget.grid(row = row, column = column, **kwargs)

    # @staticmethod
    # def pack(widget: Widget, ):

    def _set_initial_window(self):
        center_x = (self.winfo_screenwidth() // 2) - 300
        center_y = (self.winfo_screenheight() // 2) - 260
        self.title("Fantasia - v1.0")
        self.geometry(f"600x520+{center_x}+{center_y}")
        self.resizable(False, False)
        # self.minsize(400, 800)
        # self.maxsize(400, 800)

    def _set_key_bind(self):
        self.bind("<Control-Alt-F12>", self._show_admin_controller)

    def _set_var(self):
        self._components.add_string_var("current_user")
        self._components.set_string_var_value("current_user", "RED")  # default 값 지정
        self._components.add_string_var("user_card")
        self._components.set_string_var_value("user_card", "herbs")
        self._components.add_string_var("card_name")
        self._components.set_string_var_value("card_name", "없음")
        self._components.add_string_var("card_level")
        self._components.set_string_var_value("card_level", "1")
        self._set_var_tracer()

    def _set_var_tracer(self):
        self._components.get_string_var("user_card").trace_add(
            mode = "write",
            callback = self._update_card_names
        )

        self._components.get_string_var("current_user").trace_add(
            mode = "write",
            callback = self._update_labels_data
        )

    def _render_component(self):
        self._set_frame()  # 1순위
        self._set_label_frame()  # 2순위
        self._set_option_menu()  # 3순위
        self._set_label()  # 3순위
        self._set_button()  # 3순위

    def _set_frame(self):
        datas_frame = Frame(self)
        datas_frame.pack(side = "top", anchor = "center")

        funcs_frame = Frame(self)
        funcs_frame.pack(side = "top", anchor = "center", pady = 10)

        button_frame = Frame(self)
        button_frame.pack(side = "top", anchor = "center")

        change_round_btn_frame = Frame(button_frame)
        change_round_btn_frame.grid(row = 0, column = 0, padx = 50)

        trade_btn_frame = Frame(button_frame)
        trade_btn_frame.grid(row = 0, column = 1, padx = 50)

        self._components.add_frame("datas_frame", datas_frame)
        self._components.add_frame("funcs_frame", funcs_frame)
        self._components.add_frame("button_frame", button_frame)
        self._components.add_frame("trade_btn_frame", trade_btn_frame)
        self._components.add_frame("change_round_btn_frame", change_round_btn_frame)

    def _set_label_frame(self):
        funcs_frame = self._components.get_frame("funcs_frame")
        datas_frame = self._components.get_frame("datas_frame")

        herbs_label_frame = LabelFrame(
            datas_frame,
            text = "마법 약초 현황"
        )
        herbs_label_frame.grid(row = 0, column = 0, padx = 5, pady = 5)
        self._components.add_label_frame("herbs_label", herbs_label_frame)

        animals_label_frame = LabelFrame(
            datas_frame,
            text = "마법 동물 현황"
        )
        animals_label_frame.grid(row = 0, column = 1, padx = 5, pady = 5)
        self._components.add_label_frame("animals_label", animals_label_frame)

        tools_label_frame = LabelFrame(
            datas_frame,
            text = "마법 도구 현황"
        )
        tools_label_frame.grid(row = 0, column = 2, padx = 5, pady = 5)
        self._components.add_label_frame("tools_label", tools_label_frame)

        user_label_frame = LabelFrame(
            datas_frame,
            text = "유저 정보"
        )
        user_label_frame.grid(row = 1, column = 1, padx = 5, pady = 5)
        self._components.add_label_frame("user_label", user_label_frame)

        game_info_label_frame = LabelFrame(
            datas_frame,
            text = "게임 정보"
        )
        game_info_label_frame.grid(row = 1, column = 2, padx = 5, pady = 5)
        self._components.add_label_frame("game_info_label", game_info_label_frame)

        select_user = LabelFrame(
            funcs_frame,
            text = "참가자 선택",
        )
        select_user.grid(row = 0, column = 0, pady = 5)
        self._components.add_label_frame("select_user", select_user)

        select_card = LabelFrame(
            funcs_frame,
            text = "카드 종류 선택"
        )
        select_card.grid(row = 0, column = 1, pady = 5)
        self._components.add_label_frame("select_card", select_card)

        card_name = LabelFrame(
            funcs_frame,
            text = "카드 이름 선택"
        )
        card_name.grid(row = 0, column = 2, pady = 5)
        self._components.add_label_frame("card_name", card_name)

        card_level = LabelFrame(
            funcs_frame,
            text = "카드 레벨 선택"
        )
        card_level.grid(row = 0, column = 3, pady = 5)
        self._components.add_label_frame("card_level", card_level)

    def _set_button(self):
        change_round_button = Button(
            self._components.get_frame("change_round_btn_frame"),
            # self._components.get_frame("button_frame"),
            text = "턴 진행",
            width = 8,
            height = 2,
            command = self.round_change
        )
        change_round_button.grid(row = 0, column = 0)
        self._components.add_button("change_round_btn", change_round_button)

        train_button = Button(
            self._components.get_frame("trade_btn_frame"),
            text = "훈련",
            width = 6,
            height = 2,
            command = self.train,
            state = "disabled"
        )

        train_button.grid(row = 0, column = 0, padx = 5, pady = 10)
        self._components.add_button("train_btn", train_button)

        buy_button = Button(
            self._components.get_frame("trade_btn_frame"),
            # self._components.get_frame("button_frame"),
            text = "구매",
            width = 6,
            height = 2,
            command = self.buy
        )
        buy_button.grid(row = 0, column = 1, padx = 5, pady = 10)
        self._components.add_button("buy_btn", buy_button)

        sell_button = Button(
            self._components.get_frame("trade_btn_frame"),
            # self._components.get_frame("button_frame"),
            text = "판매",
            width = 6,
            height = 2,
            command = self.sell,
        )

        sell_button.grid(row = 0, column = 2, padx = 5, pady = 10)
        self._components.add_button("sell_btn", sell_button)

        test_btn = Button(
            self._components.get_frame("change_round_btn_frame"),
            text = "테스트",
            width = 8,
            height = 2,
            command = self._value_test
        )
        if self._debug_mode:
            test_btn.grid()

    def _value_test(self):
        AdminController(
            master = self,
            fantasia_instance = self._fantasia
        )

    def _show_admin_controller(self, *args):
        AdminController(
            master = self,
            fantasia_instance = self._fantasia
        )
        self._update_labels_data()

    def _set_combobox(self):
        pass

    def _set_option_menu(self):
        select_user_option_menu = OptionMenu(
            self._components.get_label_frame("select_user"),
            self._components.get_string_var("current_user"),
            "RED",
            *USER_COLORS[1:]
        )
        select_user_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("select_user_option_menu", select_user_option_menu)

        user_card_option_menu = OptionMenu(
            self._components.get_label_frame("select_card"),
            self._components.get_string_var("user_card"),
            "herbs",
            *USER_CARDS[1:]
        )
        user_card_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("user_card_option_menu", user_card_option_menu)

        card_name_option_menu = OptionMenu(
            self._components.get_label_frame("card_name"),
            self._components.get_string_var("card_name"),
            "없음",
            *CARD_NAMES.get(self._get_user_card())
        )
        card_name_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("card_name_option_menu", card_name_option_menu)

        card_level_option_menu = OptionMenu(
            self._components.get_label_frame("card_level"),
            self._components.get_string_var("card_level"),
            "1",
            *["2", "3"]
        )
        card_level_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("card_level_option_menu", card_level_option_menu)

    def _set_label(self):
        current_user_data = self._fantasia.get_user(self._get_select_user())

        for idx, herb_name in enumerate(current_user_data.herbs):
            herb_data = current_user_data.herbs.get(herb_name)
            herb_data_string = f"{herb_name} : {herb_data.amount}"
            herb_label = Label(
                self._components.get_label_frame("herbs_label"),
                text = herb_data_string
            )
            herb_label.grid(row = idx, column = 0, padx = 5, pady = 5)
            self._components.add_label(f"{herb_name}_label", herb_label)

        for idx, animal_name in enumerate(current_user_data.animals):
            animal_data = current_user_data.animals.get(animal_name)
            animal_data_string = "".join([f"{animal_name} : LEVEL{i + 1} : {animal_data[i].amount}\n" for i in range(3)])
            animal_label = Label(
                self._components.get_label_frame("animals_label"),
                text = animal_data_string
            )
            animal_label.grid(row = idx - 3 if idx >= 3 else idx, column = 1 if idx >= 3 else 0, padx = 5, pady = 5)
            self._components.add_label(f"{animal_name}_label", animal_label)

        for idx, tool_name in enumerate(current_user_data.tools):
            tool_data = current_user_data.tools.get(tool_name)
            tool_data_string = (f"{tool_name} : "
                                f"{tool_data.piece}/{tool_data.need_piece} : "
                                f"{tool_data.profit if tool_data.is_activated else 0}")
            tool_label = Label(
                self._components.get_label_frame("tools_label"),
                text = tool_data_string
            )
            tool_label.grid(row = idx, column = 0, padx = 5, pady = 5)
            self._components.add_label(f"{tool_name}_label", tool_label)

        user_data_string = (f"유저 : {current_user_data.color}\n"
                            f"소유 마나 : {current_user_data.mana}\n"
                            f"다음턴 월급 : {current_user_data.get_current_round_profit()}")

        user_info_label = Label(
            self._components.get_label_frame("user_label"),
            text = user_data_string
        )
        user_info_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self._components.add_label("user_label", user_info_label)

        game_data_string = f"현재 턴 : {self._fantasia.round}턴\n종료까지 : {9 - self._fantasia.round}턴"
        game_info_label = Label(
            self._components.get_label_frame("game_info_label"),
            text = game_data_string
        )
        game_info_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self._components.add_label("game_info_label", game_info_label)

    def _update_card_names(self, *args):
        print("업데이트 함수 호출됨")
        train_button = self._components.get_button("train_btn")

        if self._get_user_card() == "animal":
            train_button.config(state = "normal")
        else:
            train_button.config(state = "disabled")

        card_name_option_menu = self._components.get_option_menu("card_name_option_menu")
        card_name_option_menu.destroy()
        card_name_option_menu = OptionMenu(
            self._components.get_label_frame("card_name"),
            self._components.get_string_var("card_name"),
            "없음",
            *CARD_NAMES.get(self._get_user_card())
        )
        card_name_option_menu.pack(padx = 5, pady = 5)
        self._components.add_option_menu("card_name_option_menu", card_name_option_menu)

    def _update_labels_data(self, *args):
        for label_name in ["user", "game_info"] + CARD_NAMES.get("herbs") + CARD_NAMES.get("animal") + CARD_NAMES.get("tool"):
            self._components.get_label(f"{label_name}_label").destroy()
        self._set_label()

        # current_user_data = self._fantasia.get_user(self._get_select_user())
        #
        # user_data_string = (f"유저 : {current_user_data.color}\n"
        #                     f"소유 마나 : {current_user_data.mana}\n"
        #                     f"다음턴 월급 : {current_user_data.get_current_round_profit()}")
        #
        # user_info_label = Label(
        #     self._components.get_label_frame("user_label"),
        #     text = user_data_string
        # )
        # user_info_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        # self._components.add_label("user_label", user_info_label)

    def _get_select_user(self) -> str:
        return self._components.get_string_var("current_user").get()

    def _get_user_card(self) -> str:
        return self._components.get_string_var("user_card").get()

    def _get_user_card_name(self) -> str:
        return self._components.get_string_var("card_name").get()

    def _get_card_level(self) -> int:
        return int(self._components.get_string_var("card_level").get())

    def buy(self):
        current_user = self._fantasia.get_user(self._get_select_user())
        current_user_card = self._get_user_card()
        dialog_string = f"{CARD_TAG_TO_KR.get(current_user_card)}을 얼마나 구매 하시겠습니까?"
        dialog_result = simpledialog.askinteger(dialog_string, "구매를 원하는 갯수 입력")
        print(f"dialog_result : {dialog_result}")
        try:
            if dialog_result:
                if current_user_card == "herbs":
                    current_user.buy_herb(
                        name = self._get_user_card_name(),
                        amount = dialog_result
                    )

                elif current_user_card == "animal":
                    current_user.buy_animal(
                        name = self._get_user_card_name(),
                        amount = dialog_result,
                        level = self._get_card_level()
                    )

                elif current_user_card == "tool":
                    current_user.buy_tool_piece(
                        name = self._get_user_card_name(),
                        amount = dialog_result
                    )
            else:
                print("구매가 취소 되었습니다.")

        except ValueError as E:
            messagebox.showinfo("에러 발생", E.__str__())

        self._update_labels_data()

    def sell(self):
        current_user = self._fantasia.get_user(self._get_select_user())
        current_user_card = self._get_user_card()
        dialog_string = f"{CARD_TAG_TO_KR.get(current_user_card)}을 얼마나 판매 하시겠습니까?"
        dialog_result = simpledialog.askinteger(dialog_string, "판매를 원하는 갯수 입력")
        print(f"dialog_result : {dialog_result}")
        try:
            if dialog_result:
                if current_user_card == "herbs":
                    current_user.sell_herb(
                        name = self._get_user_card_name(),
                        amount = dialog_result
                    )

                elif current_user_card == "animal":
                    animal_name = self._get_user_card_name()
                    animal_level = self._get_card_level()
                    if self._fantasia.is_tradeable(animal_name = animal_name, animal_level = animal_level):
                        current_user.sell_animal(
                            name = animal_name,
                            amount = dialog_result,
                            level = self._get_card_level()
                        )
                    else:
                        messagebox.showinfo("판매 불가!", "해당 마법 동물은 현재 라운드에 판매가 불가능합니다.")
                else:
                    messagebox.showinfo("판매 불가!", "마법 도구는 판매가 불가능합니다!")
            else:
                print("판매가 취소 되었습니다.")

        except ValueError as E:
            messagebox.showinfo("에러 발생", E.__str__())

        self._update_labels_data()

    def train(self):
        current_user = self._fantasia.get_user(self._get_select_user())
        current_user_card = self._get_user_card()
        dialog_string = f"{CARD_TAG_TO_KR.get(current_user_card)}을 얼마나 훈련 하시겠습니까?"
        dialog_result = simpledialog.askinteger(dialog_string, "훈련을 원하는 갯수 입력")
        print(f"dialog_result : {dialog_result}")
        try:
            if dialog_result:
                current_user.train_animal(
                    name = self._get_user_card_name(),
                    amount = dialog_result,
                    level = self._get_card_level()
                )
            else:
                print("훈련이 취소 되었습니다.")

        except ValueError as E:
            messagebox.showinfo("에러 발생", E.__str__())

        self._update_labels_data()

    def round_change(self):
        if self._fantasia.round < 9:
            self._fantasia.round_change()
            self._update_labels_data()
        else:
            messagebox.showinfo("게임 종료!", "게임 종료!")
            self._components.get_button("change_round_btn").destroy()
            self._components.get_button("buy_btn").destroy()
            self._components.get_button("sell_btn").destroy()


if __name__ == '__main__':
    FantasiaGUI()

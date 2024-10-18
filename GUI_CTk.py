
# libraries Import
from tkinter import *
import customtkinter

# Main Window Properties

window = Tk()
window.title("Tkinter")
window.geometry("600x800")
window.configure(bg="#FFFFFF")


radio_var = IntVar()

"""
 ########################################  版面配置區  ########################################
"""

# 大標 1
Title_1 = customtkinter.CTkLabel(
    master=window,
    text="欲統計分析之交易資料條件範圍",
    font=("Arial", 20),
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Title_1.place(x=50, y=0)

# 註解 1
Info_title_1 = customtkinter.CTkLabel(
    master=window,
    text="填寫說明: 輸入之條件建議盡量與目標購置之房屋條件相近，以增加預測可參考性",
    font=("Arial", 14),
    text_color="#646464",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Info_title_1.place(x=10, y=40)

# 底色框 1 =======================================================================
Label_id50 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=550,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id50.place(x=20, y=110)

# Button_id3
Button_id3 = customtkinter.CTkOptionMenu(
    master=window,
    values=["選項1", "選項2", "選項3"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=50,
    width=95,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Button_id3.place(x=20, y=120)

# Button_id4
Button_id4 = customtkinter.CTkOptionMenu(
    master=window,
    values=["選項1", "選項2", "選項3"],
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    height=50,
    width=95,
    corner_radius=6,
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Button_id4.place(x=130, y=120)

# Checkbox_id5
Checkbox_id5 = customtkinter.CTkCheckBox(
    master=window,
    text="房屋",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Checkbox_id5.place(x=250, y=110)

# Checkbox_id6
Checkbox_id6 = customtkinter.CTkCheckBox(
    master=window,
    text="土地",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Checkbox_id6.place(x=250, y=150)

# Checkbox_id7
Checkbox_id7 = customtkinter.CTkCheckBox(
    master=window,
    text="建物",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Checkbox_id7.place(x=320, y=110)

# Checkbox_id8
Checkbox_id8 = customtkinter.CTkCheckBox(
    master=window,
    text="車位",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#808080",
    corner_radius=4,
    border_width=2,
    height=30,
    width=60,
)
Checkbox_id8.place(x=320, y=150)

# Entry_id12
Entry_id12 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="門牌/社區名稱",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=50,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Entry_id12.place(x=400, y=120)


# 底色框 2 =======================================================================
Label_id51 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=550,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id51.place(x=20, y=210)

# Label_id13
Label_id13 = customtkinter.CTkLabel(
    master=window,
    text="交易期間:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=80,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id13.place(x=20, y=220)

# Entry_id14
Entry_id14 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="YYY(下拉式)",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=60,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Entry_id14.place(x=120, y=220)

# Label_id18
Label_id18 = customtkinter.CTkLabel(
    master=window,
    text="年",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id18.place(x=180, y=220)

# Entry_id15
Entry_id15 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="MM月(下拉式)",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=60,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Entry_id15.place(x=210, y=220)

# Label_id21
Label_id21 = customtkinter.CTkLabel(
    master=window,
    text="至",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id21.place(x=290, y=220)

# Entry_id16
Entry_id16 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="YYY(下拉式)",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=60,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Entry_id16.place(x=340, y=220)

# Label_id19
Label_id19 = customtkinter.CTkLabel(
    master=window,
    text="年",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id19.place(x=400, y=220)

# Entry_id17
Entry_id17 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="MM月(下拉式)",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=60,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
)
Entry_id17.place(x=430, y=220)

# Label_id22
Label_id22 = customtkinter.CTkLabel(
    master=window,
    text="止",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id22.place(x=510, y=220)

# Label_id23
Label_id23 = customtkinter.CTkLabel(
    master=window,
    text="說明2",
    font=("Arial", 14),
    text_color="#646464",
    height=30,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
)
Label_id23.place(x=20, y=260)

# 底色框 3 =======================================================================
Label_id52 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=360,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id52.place(x=20, y=300)

# Label_id24
Label_id24 = customtkinter.CTkLabel(
    master=window,
    text="單價:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id24.place(x=20, y=330)

# Label_id25
RadioButton_id25 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=25,
    text="萬元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id25.place(x=90, y=320)

# Label_id26
RadioButton_id26 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=26,
    text="元",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id26.place(x=90, y=350)

# Label_id27
Entry_id27 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id27.place(x=170, y=330)

# Label_id29
Label_id29 = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id29.place(x=260, y=330)

# Label_id28
Entry_id28 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id28.place(x=290, y=330)

# 底色框 4 =======================================================================
Label_id53 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=360,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id53.place(x=20, y=390)

# Label_id33
Label_id33 = customtkinter.CTkLabel(
    master=window,
    text="面積:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id33.place(x=20, y=400)

# Label_id34
RadioButton_id34 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=34,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id34.place(x=90, y=390)

# Label_id36
RadioButton_id36 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=36,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id36.place(x=90, y=420)

# Label_id30
Entry_id30 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最小",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id30.place(x=170, y=400)

# Label_id32
Label_id32 = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=30,
    width=25,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id32.place(x=260, y=400)

# Label_id31
Entry_id31 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="最大",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=30,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id31.place(x=290, y=400)

# 底色框 5 =======================================================================
Label_id54 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=200,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id54.place(x=390, y=340)

# Label_id37
Label_id37 = customtkinter.CTkLabel(
    master=window,
    text="屋齡:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id37.place(x=400, y=360)

# Label_id38
Button_id38 = customtkinter.CTkButton(
    master=window,
    text="下拉式選單",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=40,
    width=95,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id38.place(x=470, y=360)

# 底色框 6 =======================================================================
Label_id55 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=60,
    width=350,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id55.place(x=20, y=510)

# Label_id39
Label_id39 = customtkinter.CTkLabel(
    master=window,
    text="目標購置之房屋資訊",
    font=("Arial", 20),
    text_color="#000000",
    height=40,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id39.place(x=0, y=470)

# Label_id40
Label_id40 = customtkinter.CTkLabel(
    master=window,
    text="時間:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id40.place(x=20, y=520)

# Label_id41
Button_id41 = customtkinter.CTkButton(
    master=window,
    text="下拉式選單",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=40,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id41.place(x=110, y=520)

# Label_id42
Label_id42 = customtkinter.CTkLabel(
    master=window,
    text="~",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=30,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id42.place(x=200, y=520)

# Label_id43
Button_id43 = customtkinter.CTkButton(
    master=window,
    text="下拉式選單",
    font=("undefined", 14),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=40,
    width=80,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Button_id43.place(x=240, y=520)

# 底色框 7 =======================================================================
Label_id57 = customtkinter.CTkLabel(
    master=window,
    text=" ",
    font=("Arial", 14),
    text_color="#000000",
    height=80,
    width=350,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#c8c8c8",
    )
Label_id57.place(x=20, y=580)

# Label_id44
Label_id44 = customtkinter.CTkLabel(
    master=window,
    text="面積:",
    font=("Arial", 16),
    text_color="#000000",
    height=40,
    width=60,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id44.place(x=20, y=590)

# Label_id45
RadioButton_id45 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=45,
    text="平方米",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id45.place(x=100, y=580)

# Label_id46
RadioButton_id46 = customtkinter.CTkRadioButton(
    master=window,
    variable=radio_var,
    value=46,
    text="坪",
    text_color="#000000",
    border_color="#000000",
    fg_color="#808080",
    hover_color="#2F2F2F",
    height=30,
    width=60,
    )
RadioButton_id46.place(x=100, y=610)

# Label_id47
Entry_id47 = customtkinter.CTkEntry(
    master=window,
    placeholder_text="輸入面積",
    placeholder_text_color="#454545",
    font=("Arial", 14),
    text_color="#000000",
    height=40,
    width=120,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#F0F0F0",
    )
Entry_id47.place(x=200, y=590)

"""
 ########################################  資料輸出區  ########################################
"""

# 生成資料按鈕
Button_id48 = customtkinter.CTkButton(
    master=window,
    text="生成資料",
    font=("undefined", 18),
    text_color="#000000",
    hover=True,
    hover_color="#949494",
    height=50,
    width=150,
    border_width=2,
    corner_radius=6,
    border_color="#000000",
    bg_color="#FFFFFF",
    fg_color="#75f6ff",
    )
Button_id48.place(x=200, y=660)

# 輸出區
Label_id49 = customtkinter.CTkLabel(
    master=window,
    text="輸出區",
    font=("Arial", 16),
    text_color="#0033ff",
    height=80,
    width=300,
    corner_radius=0,
    bg_color="#FFFFFF",
    fg_color="#FFFFFF",
    )
Label_id49.place(x=140, y=720)

#run the main loop
window.mainloop()


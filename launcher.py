
import customtkinter 
from tkinter import *
from tkinter.ttk import *
import time
import easygui

app = customtkinter.CTk()
app.geometry("500x600")

logined = False
wrongEntry = 0
secretpass = None


def login():
    if entry1.get() == secretpass:
        global logined
        logined = True
        app.destroy()
        import main
        main.main()
    else:
        global wrongEntry
        wrongEntry += 1
        if wrongEntry <= 1:
            label2 = customtkinter.CTkLabel(master=frame, text="密鑰錯誤", text_color="#FF0000")
            label2.pack(pady = 12, padx = 10)
def getpass():
    textbox = easygui.enterbox(msg = "")



frame = customtkinter.CTkFrame(master = app)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "輸入密鑰進入遊戲")
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text = "密鑰：")
entry1.pack(pady = 12, padx = 10)

#entry2 = customtkinter.CTkEntry(master = frame, placeholder_text = "密碼", show = "*")
#entry2.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "進入遊戲", command = login)
button.pack(pady = 12, padx = 10)

label = customtkinter.CTkLabel(master = frame, text = "沒有密鑰？")
label.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "獲取密鑰", command = getpass)
button.pack(pady = 12, padx = 10)

label = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C)\n2024 Zeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org] &\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
label.pack(pady = 12, padx = 10)

app.mainloop()


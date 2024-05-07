import customtkinter 
from tkinter import *
from tkinter.ttk import *
import time
import activation

'''
app = customtkinter.CTk()
app.geometry("500x400")

logined = False
wrongEntry = 0
def login():
    if entry1.get() == "admin" and entry2.get() == "admin":
        global logined
        logined = True
        app.destroy()
    else:
        global wrongEntry
        wrongEntry += 1
        if wrongEntry <= 1:
            label2 = customtkinter.CTkLabel(master=frame, text="用戶名稱或密碼錯誤", text_color="#FF0000")
            label2.pack(pady = 12, padx = 10)


frame = customtkinter.CTkFrame(master = app)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)

label = customtkinter.CTkLabel(master = frame, text = "進入遊戲")
label.pack(pady = 12, padx = 10)

entry1 = customtkinter.CTkEntry(master = frame, placeholder_text = "用戶名稱")
entry1.pack(pady = 12, padx = 10)

entry2 = customtkinter.CTkEntry(master = frame, placeholder_text = "密碼", show = "*")
entry2.pack(pady = 12, padx = 10)

button = customtkinter.CTkButton(master = frame, text = "登錄", command = login)
button.pack(pady = 12, padx = 10)

label = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C)\n2024 Zeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org] &\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
label.pack(pady = 12, padx = 10)

app.mainloop()
'''

activation_raw = activation.check_activation()
activation_status = False
if activation_raw != "FAIL":
    activation_status = True

#activation
while not activation_status:
    wrongEntry = 0
    def activate():
        activation.write_activation(key.get(), type.get(), name.get(), mail.get())
        activation_raw = activation.check_activation()
        if activation_raw != "FAIL":
            app.destroy()
            global wrongEntry
        else:
            wrongEntry += 1
            if wrongEntry <= 1:
                label2 = customtkinter.CTkLabel(master=frame, text="激活碼錯誤", text_color="#FF0000")
                label2.pack(pady = 12, padx = 10)
    app = customtkinter.CTk()
    app.geometry("800x600")
    frame = customtkinter.CTkFrame(master = app)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    label = customtkinter.CTkLabel(master = frame, text = "激活遊戲")
    label.pack(pady = 12, padx = 10)
    key = customtkinter.CTkEntry(master = frame, placeholder_text = "激活碼")
    key.pack(pady = 12, padx = 10)
    name = customtkinter.CTkEntry(master = frame, placeholder_text = "全名")
    name.pack(pady = 12, padx = 10)
    mail = customtkinter.CTkEntry(master = frame, placeholder_text = "電郵")
    mail.pack(pady = 12, padx = 10)
    type = customtkinter.CTkEntry(master = frame, placeholder_text = "類型")
    type.pack(pady = 12, padx = 10)
    button = customtkinter.CTkButton(master = frame, text = "激活", command = activate)
    button.pack(pady = 12, padx = 10)
    label = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label.pack(pady = 12, padx = 10)
    app.mainloop()
    activation_raw = activation.check_activation()
    if activation_raw != "FAIL":
        activation_status = True

#import main
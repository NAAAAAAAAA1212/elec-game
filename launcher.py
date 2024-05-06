'''
import easygui

open = easygui.buttonbox(msg = "開發者版本 1.0.0\n版權持有 (C) 2024 Zeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org] &\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", title = "山海合一", choices = ["Start", "Stop"], cancel_choice = "Stop")
if open is None:
    open = "Stop"

if open is "Start":
    import main

if open is "Stop":
    exit
'''
import customtkinter 
from tkinter import *
from tkinter.ttk import *
import time

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

#print(logined)
if logined:
    def start():
        progress = 0
        speed = 1
        while(progress < 100):
            time.sleep(0.05)
            bar['value']+=(speed/100)*100
            progress += speed
            window.update_idletasks()
        window.destroy()


    window = Tk()

    window.title("Game Loading.....")

    percent = StringVar()
    text = StringVar()

    bar = Progressbar(window,orient=HORIZONTAL,length=300)
    bar.pack(pady=10)

    start()

    window.mainloop()


import main
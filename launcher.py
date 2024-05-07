import customtkinter 
from tkinter import *
from tkinter.ttk import *
import time
import activation
import os

reset = False
run = False

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
    def leave():
        exit()
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
    button2 = customtkinter.CTkButton(master = frame, text = "激活", command = leave)
    button2.pack(pady = 12, padx = 10)
    label = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label.pack(pady = 12, padx = 10)
    app.mainloop()
    activation_raw = activation.check_activation()
    if activation_raw != "FAIL":
        activation_status = True

if activation_status:
    def start():
        global run
        run = True
        app.destroy()
    def leave():
        exit()
    def de():
        global reset
        reset = True
        app.destroy()
    app = customtkinter.CTk()
    app.geometry("800x600")
    frame = customtkinter.CTkFrame(master = app)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    label1 = customtkinter.CTkLabel(master = frame, text = "山海合一")
    label1.pack(pady = 12, padx = 10)
    button1 = customtkinter.CTkButton(master = frame, text = "啟動", command = start)
    button1.pack(pady = 12, padx = 10)
    button2 = customtkinter.CTkButton(master = frame, text = "退出", command = leave)
    button2.pack(pady = 12, padx = 10)
    button3 = customtkinter.CTkButton(master = frame, text = "重置", command = de)
    button3.pack(pady = 12, padx = 10)
    label2 = customtkinter.CTkLabel(master=frame, text="激活版本: "+activation_raw, text_color="#000000")
    label2.pack(pady = 12, padx = 10)
    label3 = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label3.pack(pady = 12, padx = 10)
    app.mainloop()

if reset:
    def confirm():
        os.remove("./activation/key.act")
        os.remove("./activation/mail.act")
        os.remove("./activation/name.act")
        os.remove("./activation/type.act")
        exit()
    def leave():
        exit()
    def de():
        reset = True
        app.destroy
    app = customtkinter.CTk()
    app.geometry("800x600")
    frame = customtkinter.CTkFrame(master = app)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    label1 = customtkinter.CTkLabel(master = frame, text = "重置所有設定")
    label1.pack(pady = 12, padx = 10)
    label2 = customtkinter.CTkLabel(master = frame, text = "警告: 這會清除激活碼！")
    label2.pack(pady = 12, padx = 10)
    button1 = customtkinter.CTkButton(master = frame, text = "確定", command = confirm)
    button1.pack(pady = 12, padx = 10)
    button2 = customtkinter.CTkButton(master = frame, text = "取消", command = leave)
    button2.pack(pady = 12, padx = 10)
    label2 = customtkinter.CTkLabel(master=frame, text="激活版本: "+activation_raw, text_color="#000000")
    label2.pack(pady = 12, padx = 10)
    label3 = customtkinter.CTkLabel(master=app, text="開發者版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label3.pack(pady = 12, padx = 10)
    app.mainloop()

if run:
    import main
    main.main()
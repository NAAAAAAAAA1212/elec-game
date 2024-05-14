import customtkinter 
from tkinter import *
from tkinter.ttk import *

activation_raw = "BETA"
run = False
if not run:
    def start():
        global run
        run = True
        app.destroy()
    def leave():
        exit()
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
    label2 = customtkinter.CTkLabel(master=frame, text="激活版本: "+activation_raw, text_color="#000000")
    label2.pack(pady = 12, padx = 10)
    label3 = customtkinter.CTkLabel(master=app, text="開發者公測版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label3.pack(pady = 12, padx = 10)
    app.mainloop()

if not run:
    exit()


budget = 0
infinity_budget = False
wrongEntry2 = 0
while budget == 0 and not infinity_budget:
    def leave():
        exit()
    def budget_set():
        good = False
        try:
            global budget
            budget = int(text1.get())
            good = True
        except:
            global wrongEntry2
            wrongEntry2 += 1
            if wrongEntry2 <= 1:
                label5 = customtkinter.CTkLabel(master=frame, text="預算輸入錯誤", text_color="#FF0000")
                label5.pack(pady = 12, padx = 10)
        if good:
            app.destroy()
    def infinity():
        global infinity_budget
        infinity_budget = True
        app.destroy()
    app = customtkinter.CTk()
    app.geometry("800x600")
    frame = customtkinter.CTkFrame(master = app)
    label1 = customtkinter.CTkLabel(master = frame, text = "山海合一")
    label1.pack(pady = 12, padx = 10)
    label2 = customtkinter.CTkLabel(master = frame, text = "請輸入你想要的預算")
    label2.pack(pady = 12, padx = 10)
    frame = customtkinter.CTkFrame(master = app)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    text1 = customtkinter.CTkEntry(master = frame, placeholder_text = "預算")
    text1.pack(pady = 12, padx = 10)
    button1 = customtkinter.CTkButton(master = frame, text = "我要這些預算", command = budget_set)
    button1.pack(pady = 12, padx = 10)
    button2 = customtkinter.CTkButton(master = frame, text = "我要無限預算", command = infinity)
    button2.pack(pady = 12, padx = 10)
    button3 = customtkinter.CTkButton(master = frame, text = "關閉遊戲", command = leave)
    button3.pack(pady = 12, padx = 10)  
    label3 = customtkinter.CTkLabel(master=frame, text="激活版本: "+activation_raw, text_color="#000000")
    label3.pack(pady = 12, padx = 10)
    label4 = customtkinter.CTkLabel(master=app, text="開發者公測版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label4.pack(pady = 12, padx = 10)
    app.mainloop()
wrongEntry2 = 0
point_elec = 0.0
point_newe = 0.0
while point_elec == 0.0 and point_newe == 0.0:
    app = customtkinter.CTk()
    app.geometry("800x600")
    def check():
        global wrongEntry2
        try:
            if float(text1.get()) + float(text2.get()) == 100:
                try:
                    global point_elec
                    global point_newe
                    point_elec = float(text1.get())
                    point_newe = float(text2.get())
                    app.destroy()
                except:
                    wrongEntry2 += 1
                    if wrongEntry2 <= 1:
                        label5 = customtkinter.CTkLabel(master=frame, text="分數佔比輸入錯誤", text_color="#FF0000")
                        label5.pack(pady = 12, padx = 10)
            else:
                wrongEntry2 += 1
                if wrongEntry2 <= 1:
                    label5 = customtkinter.CTkLabel(master=frame, text="分數佔比輸入錯誤", text_color="#FF0000")
                    label5.pack(pady = 12, padx = 10)
        except:
            wrongEntry2 += 1
            if wrongEntry2 <= 1:
                label2 = customtkinter.CTkLabel(master=frame, text="分數佔比輸入錯誤", text_color="#FF0000")
                label2.pack(pady = 12, padx = 10)
    def leave():
        exit()
    frame = customtkinter.CTkFrame(master = app)
    frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
    label1 = customtkinter.CTkLabel(master = frame, text = "山海合一")
    label1.pack(pady = 12, padx = 10)
    label2 = customtkinter.CTkLabel(master = frame, text = "請設置分數佔比")
    label2.pack(pady = 12, padx = 10)
    text1 = customtkinter.CTkEntry(master = frame, placeholder_text = "能源輸出佔比")
    text1.pack(pady = 12, padx = 10)
    text2 = customtkinter.CTkEntry(master = frame, placeholder_text = "環境輸出佔比")
    text2.pack(pady = 12, padx = 10)
    button1 = customtkinter.CTkButton(master = frame, text = "分數設置", command = check)
    button1.pack(pady = 12, padx = 10)
    button2 = customtkinter.CTkButton(master = frame, text = "關閉遊戲", command = leave)
    button2.pack(pady = 12, padx = 10)  
    label3 = customtkinter.CTkLabel(master=frame, text="激活版本: "+activation_raw, text_color="#000000")
    label3.pack(pady = 12, padx = 10)
    label4 = customtkinter.CTkLabel(master=app, text="開發者公測版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
    label4.pack(pady = 12, padx = 10)
    app.mainloop()

import main
point = main.main(budget, infinity_budget, point_elec, point_newe)
app = customtkinter.CTk()
app.geometry("800x600")
def bye():
    exit()
frame = customtkinter.CTkFrame(master = app)
frame.pack(pady = 20, padx = 60, fill = "both", expand = True)
label1 = customtkinter.CTkLabel(master = frame, text = "山海合一")
label1.pack(pady = 12, padx = 10)
label2 = customtkinter.CTkLabel(master = frame, text = "遊戲結束!")
label2.pack(pady = 12, padx = 10)
label3 = customtkinter.CTkLabel(master = frame, text = "你的分數是:")
label3.pack(pady = 12, padx = 10)
label4 = customtkinter.CTkLabel(master = frame, text = point)
label4.pack(pady = 12, padx = 10)
button1 = customtkinter.CTkButton(master = frame, text = ">>>結束<<<", command = bye)
button1.pack(pady = 12, padx = 10)
label5 = customtkinter.CTkLabel(master=app, text="開發者公測版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", text_color="#000000")
label5.pack(pady = 12, padx = 10)
app.mainloop()

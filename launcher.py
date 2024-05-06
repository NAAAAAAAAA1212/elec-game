import easygui

open = easygui.buttonbox(msg = "開發者版本 1.0.0\n版權持有 (C) 2024 Zeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org] &\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]", title = "山海合一", choices = ["Start", "Stop"], cancel_choice = "Stop")
if open is None:
    open = "Stop"

if open is "Start":
    import main

if open is "Stop":
    exit
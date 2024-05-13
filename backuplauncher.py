print("開發者公測版本 1.0.0\n版權持有 (C) 2024\nZeng Alexandre Qizhi [alexa@microsoft.zengqizhi.eu.org]\n&\nJiang Bo Hong [jerry@microsoft.zengqizhi.eu.org]")
print("要不要無限預算？ [Y/N]")
unlimited_raw = "NA"
while unlimited_raw != "Y" and unlimited_raw != "N":
    unlimited_raw = input("[Y/N] >>> ")
    if unlimited_raw == "Y":
        unlimitwed = True
    else:
        unlimitwed = False
budget = 0
if not unlimited_raw:
    print("要多少預算?")
    while budget == 0:
        unlimited_raw = input(" >>> ")
        try:
            budget = int(unlimited_raw)
        except:
            pass
print("請輸入分數比例:")
elec = 0
newe = 0
while elec + newe != 100:
    elec_raw = input("elec >>> ")
    newe_raw = input("newe >>> ")
    try:
        elec = int(elec_raw)
        newe = int(newe_raw)
    except:
        pass
        
print("-----------")
print("starting game......")
import main
result = main.main(budget, unlimitwed, elec, newe)
print("GAME ENDDED")
print("-----------")
print("你的分數是：" + str(result))
input("按回車結束遊戲")
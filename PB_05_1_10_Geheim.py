# ========================================================
# ==================== Achtung GEHEIM ==================== 
# ========================================================
#
#    PB_5_1_10_Geheim.py
#
# Musterprogramm zum Gebrauch von Geheim-Daten (z.B. WLAN
# oder Mail- Passworten) in MicroPython-Programmen.
#
# Kann getestet werden durch Programm:
#     Hauptprogramm_Geheim.py
# muss ...
#     dort als Bibliothek importiert werden, und
#     auf Pico geladen sein.
# ========================================================

#
def WLAN_SSID():
    return "FB_7520"
def WLAN_PW():
    return "12345678901234567890"
def Mail_Adresse():
    return "dieter.carbon@comidio.de"
def Mail_PW():
    return "doedeldoedeldoedel"

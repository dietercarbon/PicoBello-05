#==========================================================================
#
#  PB-5-1-20-Hauptprogramm-Geheim.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliothek(en) laden
from PB_05_1_10_Geheim import WLAN_SSID, WLAN_PW, Mail_Adresse, Mail_PW

print("WLAN_SSID =",WLAN_SSID())
print("WLAN_PW =",WLAN_PW())
print()
print("Mail_Adresse =",Mail_Adresse())
print("Mail_PW =",Mail_PW())
print("\n... usw.\n")

wlanSSID = WLAN_SSID()
wlanPW = WLAN_PW()

print(wlanSSID,wlanPW)

# im "echten" Programm werden nur die Zeilen 13, 22 und 23 benötigt.


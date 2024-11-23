#==========================================================================
#
# PB-5-2-20-ElKo-WLAN-Verbindungsstatus ermitteln.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
import network
import rp2
import utime as time
from utime import sleep
from DCpriv import DCwlanSSID, DCwlanPW

# WLAN-Konfiguration
wlanSSID = DCwlanSSID()
wlanPW = DCwlanPW()
#wlanSSID = 'WLANNAME'
#wlanPW = 'WLANPASSWORD'
rp2.country('DE')

# WLAN-Verbindung herstellen
wlan = network.WLAN(network.STA_IF)
if not wlan.isconnected():
    print('WLAN-Verbindung herstellen')
    wlan.active(True)
    wlan.connect(wlanSSID, wlanPW)
    sleep(5)

# WLAN-Verbindung prüfen
if wlan.isconnected():
    print('WLAN-Verbindung hergestellt')
else:
    print('Keine WLAN-Verbindung')

# WLAN-Verbindungsstatus
print('WLAN-Status:', wlan.status())

"""
Das vorliegende Programm ist in der Programmiersprache MicroPython geschrieben
und läuft auf einem Raspberry Pi Pico. Es hat den Zweck, den WLAN-
Verbindungsstatus des Pico zu überprüfen und auszugeben.

Das Programm beginnt mit dem Laden der benötigten Bibliotheken. Hier werden
die Bibliotheken network, rp2 und utime importiert, wobei sleep aus utime
importiert wird.

Anschließend werden in den Zeilen 8 und 9 die WLAN-SSID und das WLAN-Passwort
aus einer separaten Datei namens "DCpriv.py" importiert.

In Zeile 12 wird das Land auf Deutschland (DE) eingestellt, was für eine
korrekte WLAN-Kommunikation wichtig sein kann.

In den Zeilen 15-20 wird eine WLAN-Verbindung hergestellt, falls noch keine
Verbindung besteht. Hier wird der Status der WLAN-Verbindung überprüft
(wlan.isconnected()) und falls keine Verbindung besteht, wird die Verbindung
mit der angegebenen SSID und dem angegebenen Passwort hergestellt
(wlan.connect(wlanSSID, wlanPW)). Nach dem Herstellen der Verbindung
wird ein kurzer Delay von 5 Sekunden eingebaut (sleep(5)).

In den Zeilen 23-26 wird der WLAN-Verbindungsstatus erneut geprüft und je
nach Ergebnis wird eine entsprechende Meldung ausgegeben.

Schließlich wird in Zeile 29 der WLAN-Status ausgegeben, der den genauen
Status der WLAN-Verbindung angibt.

Zusammenfassend kann gesagt werden, dass das Programm den WLAN-Verbindungsstatus
überprüft und diesen ausgibt. Es wird eine Verbindung mit der angegebenen SSID
und dem angegebenen Passwort hergestellt, falls noch keine Verbindung besteht,
und der Status der Verbindung wird am Ende des Programms ausgegeben. Es ist
zu beachten, dass die WLAN-Verbindung abhängig von den örtlichen Bedingungen
und dem Netzwerk-Setup variieren kann.
"""

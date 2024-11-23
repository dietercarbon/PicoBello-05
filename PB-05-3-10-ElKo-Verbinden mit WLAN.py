#==========================================================================
#
# PB-5-3-10-ElKo-Verbinden mit WLAN.py
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

# Client-Betrieb
wlan = network.WLAN(network.STA_IF)

# WLAN-Interface aktivieren
wlan.active(True)

# WLAN-Verbindung herstellen
wlan.connect(wlanSSID, wlanPW)

# WLAN-Verbindungsstatus prüfen
import utime as time
print('Warten auf WLAN-Verbindung')
while not wlan.isconnected() and wlan.status() >= 0:
    time.sleep(1)
print('WLAN-Verbindung hergestellt / Status:', wlan.status())

"""
Das vorliegende Programm ist in der Programmiersprache MicroPython geschrieben
und läuft auf einem Raspberry Pi Pico. Es hat den Zweck, eine WLAN-Verbindung
mit einer angegebenen SSID und einem Passwort herzustellen und den Status der
Verbindung auszugeben.

Das Programm beginnt mit dem Laden der benötigten Bibliotheken. Hier werden
die Bibliotheken network, rp2 und utime importiert, wobei sleep aus utime
importiert wird.

Anschließend werden in den Zeilen 8 und 9 die WLAN-SSID und das WLAN-Passwort
aus einer separaten Datei namens "DCpriv.py" importiert.

In Zeile 12 wird das Land auf Deutschland (DE) eingestellt, was für eine
korrekte WLAN-Kommunikation wichtig sein kann.

In den Zeilen 15-17 wird das WLAN-Interface aktiviert und eine Verbindung
mit der angegebenen SSID und dem angegebenen Passwort hergestellt
(wlan.connect(wlanSSID, wlanPW)).

In den Zeilen 20-25 wird der Status der WLAN-Verbindung geprüft, indem eine
Schleife ausgeführt wird, die solange läuft, bis eine Verbindung hergestellt
wurde (while not wlan.isconnected() and wlan.status() >= 0:). Innerhalb dieser
Schleife wird ein kurzes Delay von 1 Sekunde (time.sleep(1)) eingebaut, um
den Prozessor zu entlasten. Sobald eine Verbindung hergestellt wurde, wird
eine entsprechende Meldung ausgegeben
(print('WLAN-Verbindung hergestellt / Status:', wlan.status())).

Zusammenfassend kann gesagt werden, dass das Programm eine WLAN-Verbindung
mit der angegebenen SSID und dem angegebenen Passwort herstellt und den
Status der Verbindung ausgibt. Es wird eine Schleife ausgeführt, um den
Status der Verbindung zu überprüfen, und eine entsprechende Meldung wird
ausgegeben, sobald eine Verbindung hergestellt wurde. Es ist zu beachten,
dass die WLAN-Verbindung abhängig von den örtlichen Bedingungen und dem
Netzwerk-Setup variieren kann.
"""

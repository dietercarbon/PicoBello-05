#==========================================================================
#
# PB-5-3-20-ElKo-Beenden WLAN-Verbindung.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
import network
import utime as time

# Client-Betrieb
wlan = network.WLAN(network.STA_IF)

# WLAN-Verbindung beenden
if wlan.isconnected():
    wlan.disconnect()
    time.sleep(2)
    print('WLAN-Verbindung beendet')

# WLAN-Verbindungsstatus
print('WLAN-Status:', wlan.status())

"""
Das Programm dient dazu, die WLAN-Verbindung eines Raspberry Pi Pico zu
steuern. Es besteht aus einer Reihe von Python-Anweisungen, die nacheinander
ausgeführt werden.

Das Programm beginnt mit der Importierung der Bibliotheken network und utime,
die für die Netzwerkkommunikation und Zeitsteuerung verwendet werden. Dann
wird die WLAN-Konfiguration definiert, die die WLAN-SSID und das WLAN-Passwort
enthält. Die Werte für diese Variablen werden aus der Datei DCpriv.py importiert.

Anschließend wird das WLAN-Interface aktiviert und die Verbindung mit dem WLAN
hergestellt. Das Programm überprüft dann den WLAN-Verbindungsstatus und gibt
eine entsprechende Meldung aus, ob eine Verbindung besteht oder nicht.

In der zweiten Variante des Programms wird eine Schleife verwendet, um auf
die WLAN-Verbindung zu warten, bis sie erfolgreich aufgebaut ist. Das Programm
wartet so lange, bis eine Verbindung hergestellt ist und gibt dann eine
entsprechende Meldung aus.

Das letzte Programm beendet die WLAN-Verbindung, falls sie aktiv ist. Es gibt
dann den WLAN-Verbindungsstatus aus.

Insgesamt ist das Programm einfach und gut strukturiert. Es besteht aus einer
Reihe von Anweisungen, die nacheinander ausgeführt werden, um die
WLAN-Verbindung des Raspberry Pi Pico zu steuern.
"""
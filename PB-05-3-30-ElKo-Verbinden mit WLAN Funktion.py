#==========================================================================
#
# PB-5-3-30-ElKo-Verbinden mit WLAN Funktion.py
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

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

# Funktion: WLAN-Verbindung
def wlanConnect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            led_onboard.toggle()
            print('.', wlan.status())
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        led_onboard.on()
        print('WLAN-Status:', wlan.status())
        netConfig = wlan.ifconfig()
        print('IPv4-Adresse:', netConfig[0], '/', netConfig[1])
        print('Standard-Gateway:', netConfig[2])
        print('DNS-Server:', netConfig[3])
    else:
        print('Keine WLAN-Verbindung')
        led_onboard.off()
        print('WLAN-Status:', wlan.status())

# WLAN-Verbindung herstellen
wlanConnect()

"""
Das Programm ist in Python geschrieben und läuft auf dem Raspberry Pi Pico.
Es dient dazu, eine WLAN-Verbindung herzustellen und den Verbindungsstatus
zu überprüfen.

Der Programmcode ist in vier Abschnitte unterteilt:

    Bibliotheken laden: In diesem Abschnitt werden die erforderlichen
    Bibliotheken importiert. Es werden die Bibliotheken network, rp2,
    utime und sleep geladen. Darüber hinaus wird eine benutzerdefinierte
    Bibliothek DCpriv importiert, die die WLAN-Konfiguration enthält.

    WLAN-Konfiguration: Hier werden die WLAN-Parameter wie SSID und
    Passwort aus der DCpriv-Bibliothek geladen und das Länderkürzel DE für
    die Funkregulierung festgelegt.

    Status-LED: Es wird eine Status-LED definiert, die auf dem Board vorhanden
    ist, um den Verbindungsstatus anzuzeigen.

    Funktion: WLAN-Verbindung: Hier wird eine Funktion wlanConnect definiert,
    die die WLAN-Verbindung herstellt und den Verbindungsstatus ausgibt.
    Innerhalb der Funktion wird das WLAN-Interface aktiviert, die Verbindung
    zur SSID mit dem Passwort hergestellt und der Verbindungsstatus überwacht.
    Während des Verbindungsaufbaus blinkt die Status-LED und der
    Verbindungsstatus wird über die serielle Konsole ausgegeben.

    WLAN-Verbindung herstellen: Hier wird die Funktion wlanConnect
    aufgerufen, um die WLAN-Verbindung herzustellen.

Zusammenfassend handelt es sich bei dem Programm um eine nützliche Funktion,
die es ermöglicht, eine WLAN-Verbindung auf dem Raspberry Pi Pico herzustellen
und den Verbindungsstatus anzuzeigen. Die Status-LED bietet eine visuelle
Rückmeldung über den Verbindungsstatus und die serielle Konsole gibt
detaillierte Informationen über die Verbindung aus. Der Programmcode ist
gut strukturiert und leicht verständlich.
"""
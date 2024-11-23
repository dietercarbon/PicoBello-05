#==========================================================================
#
# PB-5-6-11-ElKo-Pico W Wetterstation mit Vorhersage plus.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
import machine
import network
import rp2
import urequests as requests
import utime as time
from DCpriv import DCwlanSSID, DCwlanPW

# WLAN-Konfiguration
wlanSSID = 'Johanna2'
wlanPW = DCwlanPW()
rp2.country('DE')

# DWD-API
dwdStationID = 'K584'
dwdURL = 'https://app-prod-ws.warnwetter.de/v16/stationOverview?stationIds=' + dwdStationID
dwdText = ('Sonne','Sonne und leicht bewölkt','Sonne und bewölkt','Wolken','Nebel','Nebel mit Rutschgefahr','Leichter Regen','Regen','Starker Regen','Leichter Regen mit Rutschgefahr','Starker Regen mit Rutschgefahr','Regen mit vereinzeltem Schneefall','Regen mit vermehrtem Schneefall','Leichter Schneefall','Schneefall','Starker Schneefall','Wolken mit Hagel','Sonne mit leichtem Regen','Sonne mit starkem Regen','Sonne mit Regen und vereinzeltem Schneefall','Sonne mit Regen und vermehrtem Schneefall','Sonne mit vereinzeltem Schneefall','Sonne mit vermehrtem Schneefall','Sonne mit Hagel','Sonne mit starkem Hagel','Gewitter','Gewitter mit Regen','Gewitter mit starkem Regen','Gewitter mit Hagel','Gewitter mit starker Hagel','Wind')
dwdData = ''

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

# Wetter-Daten abrufen
try:
    print()
    print('HTTP-Request an', dwdURL)
    response = requests.get(dwdURL)
    print('Status-Code:', response.status_code)
    if response.status_code == 200:
        # JSON-Datensatz umwandeln
        dwdData = response.json()
    # Verbindung schließen
    response.close()
except OSError:
    print()
    print('Fehler: Keine Netzwerk-Verbindung (WLAN)')

# Daten verarbeiten und ausgeben
if (len(dwdData) > 0):
    # Daten-Verarbeitung
    tempMax = dwdData[dwdStationID][0]['temperatureMax'] / 10
    tempMin = dwdData[dwdStationID][0]['temperatureMin'] / 10
    dayDate = dwdData[dwdStationID][0]['dayDate']
    windSpeed   = dwdData[dwdStationID][0]['windSpeed'] / 10
    windDirection   = dwdData[dwdStationID][0]['windDirection'] / 10
    
    # Daten-Ausgabe
    print()
    print("Datum: ",dayDate)
    print("Windgeschwindigkeit:",windSpeed,"m/s; Windrichtung:",windDirection, "Grad")
    print("Temperatur: max. %s °C / min. %s °C" % (tempMax, tempMin))
    print()   
"""
Das Programm "PB-5-6-10-ElKo-DC-Pico W Wetterstation mit Vorhersage.py" für
Raspberry Pi Pico liest Wetterdaten von der DWD-API ab und gibt die Maximal-
und Minimaltemperatur sowie eine Beschreibung des Wetters aus.

Der Programmcode besteht aus fünf Teilen:

    Importieren von Bibliotheken, einschließlich der Bibliotheken machine,
        network, rp2, urequests und utime.
    Konfigurieren der WLAN-Verbindung und laden des WLAN-Passworts mit Hilfe
        der "DCpriv" Bibliothek.
    Definieren einer Funktion "wlanConnect()", die die WLAN-Verbindung
        herstellt und Status-LED einschaltet, wenn die Verbindung hergestellt wurde.
    Abrufen von Wetterdaten über die DWD-API, indem ein HTTP-Request an die
        URL dwdURL gesendet wird.
    Verarbeiten und Ausgeben der Wetterdaten, einschließlich der Temperaturdaten
        und der Beschreibung des Wetters.

Das Programm beginnt mit dem Laden der erforderlichen Bibliotheken und der
Konfiguration der WLAN-Verbindung. Die WLAN-Konfiguration erfolgt über die
Variablen "wlanSSID" und "wlanPW".

Als nächstes wird die Funktion "wlanConnect()" definiert. Diese Funktion stellt
die WLAN-Verbindung her und gibt Informationen zur Netzwerkkonfiguration aus.
Wenn die Verbindung erfolgreich hergestellt wurde, wird die Status-LED
eingeschaltet und der Status der WLAN-Verbindung ausgegeben.

Das Programm ruft dann die Wetterdaten über die DWD-API ab und verarbeitet sie.
Die Wetterdaten werden als JSON-Datensatz zurückgegeben, der in der Variablen
"dwdData" gespeichert wird. Wenn die Verbindung fehlschlägt, wird eine
Fehlermeldung ausgegeben.

Die Verarbeitung der Wetterdaten umfasst die Extraktion der Maximal- und
Minimaltemperatur sowie der Beschreibung des Wetters aus dem JSON-Datensatz.
Diese Daten werden dann ausgegeben.

Insgesamt ist das Programm gut strukturiert und dokumentiert. Es verwendet
Bibliotheken, um wiederholte Codeblöcke zu vermeiden, und definiert eine
Funktion, um den Code aufzuteilen und die Wartbarkeit zu verbessern.
Der Code enthält auch Kommentare, die die verschiedenen Codeblöcke erklären.
"""

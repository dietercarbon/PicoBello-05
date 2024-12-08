#==========================================================================
#
# PB-05-6-12-ElKo Wetter-Vorhersage LCD.py
#
# 1 LCD Display 16x2 mit I2C-Bus
#
#==========================================================================
#
# Bibliotheken laden
import machine
from machine import I2C, Pin, Timer
from machine_i2c_lcd import I2cLcd
import network
import rp2
import urequests as requests
import utime as time
from Zugang_DC import wlanSSID, wlanPW

# WLAN-Konfiguration
# WLAN-Konfiguration
wlanSSID = wlanSSID()
wlanPW = wlanPW()
#wlanSSID = 'WLANNAME'
#wlanPW = 'WLANPASSWORD'
rp2.country('DE')

# DWD-API
dwdStationID = 'K584'
dwdURL = 'https://app-prod-ws.warnwetter.de/v16/stationOverview?stationIds=' + dwdStationID
dwdText = ('Sonne','Sonne und leicht bewölkt','Sonne und bewölkt','Wolken','Nebel','Nebel mit Rutschgefahr','Leichter Regen','Regen','Starker Regen','Leichter Regen mit Rutschgefahr','Starker Regen mit Rutschgefahr','Regen mit vereinzeltem Schneefall','Regen mit vermehrtem Schneefall','Leichter Schneefall','Schneefall','Starker Schneefall','Wolken mit Hagel','Sonne mit leichtem Regen','Sonne mit starkem Regen','Sonne mit Regen und vereinzeltem Schneefall','Sonne mit Regen und vermehrtem Schneefall','Sonne mit vereinzeltem Schneefall','Sonne mit vermehrtem Schneefall','Sonne mit Hagel','Sonne mit starkem Hagel','Gewitter','Gewitter mit Regen','Gewitter mit starkem Regen','Gewitter mit Hagel','Gewitter mit starker Hagel','Wind')
dwdData = ''

# Status-LED
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

# LCD-Initialisierung
i2c = I2C(0, sda=Pin(20), scl=Pin(21), freq=100000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

def lcd_schreiben(zeile1, zeile2):
    """Text auf das LCD schreiben."""
    lcd.clear()
    lcd.move_to(0, 0)
    lcd.putstr(zeile1)
    lcd.move_to(0, 1)
    lcd.putstr(zeile2)


# Funktion: WLAN-Verbindung
def wlanConnect():
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        print('WLAN-Verbindung herstellen')
        wlan.active(True)
        wlan.connect(wlanSSID, wlanPW)
        lcd_schreiben("WLAN", "im Aufbau ...")
        for i in range(10):
            if wlan.status() < 0 or wlan.status() >= 3:
                break
            led_onboard.toggle()
            print('.', wlan.status())
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt')
        lcd_schreiben("WLAN", "verbunden!")
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

k=60

while True:
    # die Anzeigen dauern ca. 4*(5+3)=32 sek
    # wenn Rnden-Zähler k 60 erreicht, ist halbe Stunde um
    # Wetter-Daten abrufen
    if k>= 60:
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
        k=0

    # Daten verarbeiten und ausgeben
    if (len(dwdData) > 0):
        print("k = ",k)
        # Daten-Verarbeitung
        date =    dwdData[dwdStationID][0]['dayDate']
        tempMax = dwdData[dwdStationID][0]['temperatureMax'] / 10
        tempMin = dwdData[dwdStationID][0]['temperatureMin'] / 10
        icon2   = dwdData[dwdStationID][0]['icon2']
        # Daten-Ausgabe
        print()
        print(date)
        print("Temperatur: max. %s °C / min. %s °C" % (tempMax, tempMin))
        print(dwdText[icon2])
        #LCD
        lcd_schreiben("heute "+str(date),"max="+str(int(tempMax+0.5))+" min="+str(int(tempMin+0.5)))
        time.sleep(3)
        lcd_schreiben("heute "+str(date),f"{str(dwdText[icon2])[:16]}")
        time.sleep(5)

        
    # Daten-Verarbeitung
        date =    dwdData[dwdStationID][1]['dayDate']
        tempMax = dwdData[dwdStationID][1]['temperatureMax'] / 10
        tempMin = dwdData[dwdStationID][1]['temperatureMin'] / 10
        icon2   = dwdData[dwdStationID][1]['icon2']
        # Daten-Ausgabe
        print()
        print(date)
        print("Temperatur: max. %s °C / min. %s °C" % (tempMax, tempMin))
        print(dwdText[icon2])
        #LCD
        lcd_schreiben("+1    "+str(date),"max="+str(int(tempMax+0.5))+" min="+str(int(tempMin+0.5)))
        time.sleep(3)
        lcd_schreiben("+1    "+str(date),f"{str(dwdText[icon2])[:16]}")
        time.sleep(5)
        
    # Daten-Verarbeitung
        date =    dwdData[dwdStationID][2]['dayDate']
        tempMax = dwdData[dwdStationID][2]['temperatureMax'] / 10
        tempMin = dwdData[dwdStationID][2]['temperatureMin'] / 10
        icon2   = dwdData[dwdStationID][2]['icon2']
        # Daten-Ausgabe# Daten-Ausgabe
        print()
        print(date)
        print("Temperatur: max. %s °C / min. %s °C" % (tempMax, tempMin))
        print(dwdText[icon2])
        #LCD
        lcd_schreiben("+2    "+str(date),"max="+str(int(tempMax+0.5))+" min="+str(int(tempMin+0.5)))
        time.sleep(3)
        lcd_schreiben("+2    "+str(date),f"{str(dwdText[icon2])[:16]}")
        time.sleep(5)
        
    # Daten-Verarbeitung
        date =    dwdData[dwdStationID][3]['dayDate']
        tempMax = dwdData[dwdStationID][3]['temperatureMax'] / 10
        tempMin = dwdData[dwdStationID][3]['temperatureMin'] / 10
        icon2   = dwdData[dwdStationID][3]['icon2']
        # Daten-Ausgabe# Daten-Ausgabe
        print()
        print(date)
        print("Temperatur: max. %s °C / min. %s °C" % (tempMax, tempMin))
        print(dwdText[icon2])
        #LCD
        lcd_schreiben("+3    "+str(date),"max="+str(int(tempMax+0.5))+" min="+str(int(tempMin+0.5)))
        time.sleep(3)
        lcd_schreiben("+3    "+str(date),f"{str(dwdText[icon2])[:16]}")
        time.sleep(5)
        
        k=k+1
        
        
"""
# Detaillierte Erklärung des Programms

## Überblick
Das Programm verwendet einen Raspberry Pi Pico W, um Wettervorhersagedaten
für vier aufeinanderfolgende Tage von einer DWD-API abzurufen.
Die Daten werden analysiert und auf einem I2C-verbundenen LCD-Display
(16x2) dargestellt. Zusätzliche Informationen wie Temperatur und
Symbolbeschreibung werden in der Konsole ausgegeben.

---

## Hauptfunktionen

### WLAN-Verbindung
- **`wlanSSID` und `wlanPW`**: WLAN-Zugangsdaten werden aus
einer separaten Datei (`Zugang_DC`) geladen.
- **`rp2.country('DE')`**: Setzt das Land für WLAN-Standards (Deutschland).
- **`wlanConnect()`**: Verbindet den Mikrocontroller mit einem WLAN.
Der Verbindungsstatus wird auf dem LCD-Display und der Konsole angezeigt.
Es wird maximal 10 Sekunden auf eine Verbindung gewartet.

---

### Wetterdaten von der DWD-API
- **`dwdStationID`**: Gibt die Station-ID an, deren Wetterdaten abgerufen werden sollen.
- **`dwdURL`**: Die URL der API wird basierend auf der Station-ID erstellt.
- **`dwdText`**: Enthält eine Zuordnung der Wetter-Symbole zu Beschreibungen (z. B. "Sonne", "Regen").
- **`urequests`**: Wird verwendet, um HTTP-Requests an die API zu senden. 

Das Programm lädt die JSON-Daten für mehrere Tage, verarbeitet sie
und zeigt sie auf dem LCD-Display sowie in der Konsole an.

---

### LCD-Steuerung
- **`lcd_schreiben(zeile1, zeile2)`**: Schreibt zwei Zeilen Text auf das LCD.
Das Display wird vor jeder neuen Anzeige gelöscht, um die Lesbarkeit zu verbessern.

---

## Ablauf des Programms

1. **WLAN-Verbindung herstellen**
   - Die Funktion `wlanConnect()` wird aufgerufen, um den Mikrocontroller
   mit einem WLAN zu verbinden.
   - Statusinformationen werden auf dem LCD-Display angezeigt.
   
2. **Wetterdaten abrufen**
   - Alle 60 Iterationen der Hauptschleife (entspricht ca. 30 Minuten)
   wird ein HTTP-Request an die DWD-API gesendet.
   - Die JSON-Daten werden verarbeitet und lokal gespeichert.

3. **Daten anzeigen**
   - Für jeden der nächsten vier Tage (heute + die nächsten drei Tage) werden
   folgende Daten verarbeitet und ausgegeben:
     - Datum
     - Maximale und minimale Temperatur (auf ganze Zahlen gerundet).
     - Beschreibung des Wetters basierend auf dem API-Symbol.
   - Daten werden sowohl in der Konsole ausgegeben als auch auf dem LCD-Display angezeigt.
   - Jede Anzeige dauert ca. 8 Sekunden (3 Sekunden für Temperatur, 5 Sekunden für Wetterbeschreibung).

4. **Endlosschleife**
   - Die Wetteranzeige läuft kontinuierlich.
   - Alle 30 Minuten werden neue Daten von der API abgerufen.

---

## Variablen und Komponenten

### Variablen
- **`k`**: Zählt die Anzahl der Iterationen der Hauptschleife.
Nach 60 Iterationen (ca. 30 Minuten) wird ein neuer API-Request ausgelöst.
- **`dwdData`**: Enthält die abgerufenen Wetterdaten als JSON-Objekt.

### Hardware
- **Onboard-LED**: Blinkt während der WLAN-Verbindungsherstellung und
bleibt eingeschaltet, wenn die Verbindung erfolgreich ist.
- **I2C-LCD**: Wird zur Anzeige der Wetterdaten verwendet.

---

## Fehlerbehandlung
- **WLAN-Verbindung**: Falls keine WLAN-Verbindung hergestellt werden kann,
wird dies auf dem LCD und in der Konsole angezeigt. Das Programm bleibt jedoch funktionsfähig.
- **HTTP-Request**: Falls der API-Request fehlschlägt, wird ein Fehler in der Konsole ausgegeben.

---

## Erweiterungsmöglichkeiten
1. **Sommerzeit berücksichtigen**: Zeitzonenanpassungen können hinzugefügt werden.
2. **Erweiterte Fehlerbehandlung**: Verbesserte Rückmeldungen bei WLAN- oder API-Problemen.
3. **Weitere Wetterdaten**: Zusätzliche Informationen wie Windgeschwindigkeit könnten angezeigt werden.
4. **Energiesparmodus**: Automatische Reduzierung der Anzeigefrequenz im Akkubetrieb.

---

## Zusammenfassung
Das Programm zeigt, wie ein Mikrocontroller mit WLAN und einem LCD-Display
Wetterdaten abrufen und verarbeiten kann. Es kombiniert Netzwerkoperationen,
Datenverarbeitung und Hardwaresteuerung in einer kompakten Anwendung. 
"""


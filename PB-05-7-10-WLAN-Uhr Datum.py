# Bibliotheken laden
import machine
from machine import I2C, Pin, Timer
from machine_i2c_lcd import I2cLcd
import utime
import network
import ntptime
from Zugang_DC import wlanSSID, wlanPW

# WLAN-Konfiguration
WLAN_SSID = wlanSSID()
WLAN_PASSWORD = wlanPW()

# Zeitzone
TZ_OFFSET = 1  # UTC+1 für Deutschland (ohne Sommerzeit)

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

# WLAN-Verbindung herstellen
def wlan_verbinden():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WLAN_SSID, WLAN_PASSWORD)
    lcd_schreiben("WLAN", "im Aufbau ...")
    for _ in range(10):  # Maximal 5 Sekunden warten
        if wlan.isconnected():
            lcd_schreiben("WLAN", "verbunden!")
            return wlan
        utime.sleep(0.5)
    lcd_schreiben("WLAN-Fehler", "Keine Verbindung")
    return None

# Zeit synchronisieren (sekundengenau)
def synchronisiere_zeit():
    wlan = wlan_verbinden()
    if wlan and wlan.isconnected():
        try:
            ntptime.host = "pool.ntp.org"  # NTP-Server
            ntptime.settime()  # Zeit synchronisieren
            lcd_schreiben("synchronisiert", "")
            # Warte, bis die Zeit auf den Beginn der nächsten Minute einrastet
            jetzt = utime.time()
            rest = 60 - (jetzt % 60)
            print(f"Warte {rest} Sekunden bis zur nächsten Minute...")
            lcd_schreiben(str(rest)+" Sek bis Start", "ganze Minute.")
            utime.sleep(rest)
        except Exception as e:
            lcd_schreiben("NTP-Fehler", str(e))
        finally:
            wlan.disconnect()
            wlan.active(False)
    else:
        lcd_schreiben("Zeit Sync fehlg.", "WLAN-Problem")

# Datum und Uhrzeit anzeigen
def zeige_datum_und_uhrzeit(timer):
    jetzt = utime.localtime(utime.time() + TZ_OFFSET * 3600)
    datum = f"{jetzt[2]:02d}.{jetzt[1]:02d}.{jetzt[0]}"  # Format: TT.MM.JJJJ
    uhrzeit = f"{jetzt[3]:02d}:{jetzt[4]:02d}:{jetzt[5]:02d}"  # Format: HH:MM:SS
    lcd_schreiben(f"Datum {datum}", f"Zeit    {uhrzeit}")
    print(f"Datum: {datum}, Zeit: {uhrzeit}")

# Timer für regelmäßige Anzeige-Aktualisierung
zeit_timer = Timer(-1)

def starte_timer():
    zeit_timer.init(period=1000, mode=Timer.PERIODIC, callback=zeige_datum_und_uhrzeit)

# Hauptprogramm
def main():
    synchronisiere_zeit()  # Initiale Zeit-Synchronisation
    starte_timer()         # Starte die Anzeige mit sekundengenauem Timer
    startzeit = utime.time()

    while True:
        # Jede Stunde Zeit synchronisieren
        if utime.time() - startzeit >= 3600:
            synchronisiere_zeit()
            startzeit = utime.time()
        utime.sleep(1)

# Programm starten
main()


"""
# Detaillierte Erklärung des Programms

## Überblick
Dieses Programm verbindet einen Raspberry Pi Pico W mit einem WLAN-Netzwerk, synchronisiert die Uhrzeit über einen NTP-Server (Network Time Protocol) und zeigt die aktuelle Zeit und das Datum auf einem LCD-Display an. Zusätzlich wird die Zeit regelmäßig aktualisiert und stündlich neu synchronisiert. 

### Bibliotheken
- **`machine`**: Steuert die Hardware des Pico (z. B. Pins, Timer).
- **`I2C` und `Pin`**: Werden für die Kommunikation mit dem LCD-Modul über I2C verwendet.
- **`network`**: Ermöglicht die WLAN-Verbindung.
- **`ntptime`**: Dient zur Synchronisierung der Systemzeit über das Internet.
- **`utime`**: Wird für Zeitfunktionen und Verzögerungen genutzt.
- **`Zugang_DC`**: Eine benutzerdefinierte Bibliothek, die die WLAN-SSID und das Passwort bereitstellt.
- **`machine_i2c_lcd`**: Eine Bibliothek für die Steuerung eines I2C-LCD-Displays.

---

## Konfigurationsabschnitt
1. **WLAN-Konfiguration**:
   - `WLAN_SSID` und `WLAN_PASSWORD` sind die Zugangsdaten
   für das WLAN. Sie werden aus der `Zugang_DC`-Bibliothek importiert.
   
2. **Zeitzone**:
   - `TZ_OFFSET` legt die Zeitzone relativ zu UTC fest.
   Für Deutschland ohne Sommerzeit ist der Wert `1`.

3. **LCD-Initialisierung**:
   - Das LCD wird über den I2C-Bus mit den Pins 20 (SDA) und 21 (SCL) verbunden.
   - Das LCD verwendet die Adresse `0x27`, ist 2 Zeilen hoch und hat 16 Zeichen pro Zeile.

---

## Funktionen

### `lcd_schreiben(zeile1, zeile2)`
- Diese Funktion schreibt Text in zwei Zeilen auf das LCD-Display.
- Das Display wird vor jeder neuen Ausgabe gelöscht.

---

### `wlan_verbinden()`
- Verbindet den Pico mit einem WLAN-Netzwerk.
- Zeigt den Verbindungsstatus auf dem LCD an.
- Wartet bis zu 5 Sekunden, um eine Verbindung herzustellen.
- Gibt ein WLAN-Objekt zurück, wenn die Verbindung erfolgreich
ist, oder `None`, falls die Verbindung fehlschlägt.

---

### `synchronisiere_zeit()`
- Synchronisiert die Systemzeit mit einem NTP-Server.
- Wartet, bis die Zeit auf die nächste volle Minute "einrastet".
- Zeigt die verbleibenden Sekunden bis zum Start auf dem LCD an.
- Schließt die WLAN-Verbindung nach der Synchronisation.

---

### `zeige_datum_und_uhrzeit(timer)`
- Wird jede Sekunde aufgerufen, um das aktuelle Datum und die Zeit anzuzeigen.
- Berechnet das Datum und die Zeit basierend auf der lokalen Zeitzone.
- Formatiert die Anzeige auf dem LCD.

---

### `starte_timer()`
- Initialisiert einen Timer, der alle 1000 Millisekunden (1 Sekunde)
die Funktion `zeige_datum_und_uhrzeit` aufruft.

---

## Hauptprogramm

### `main()`
1. **Initiale Synchronisation**:
   - Führt eine Zeit-Synchronisation mit einem NTP-Server durch.
   
2. **Startet den Timer**:
   - Aktualisiert die Anzeige auf dem LCD jede Sekunde.

3. **Periodische Synchronisation**:
   - Synchronisiert die Zeit jede Stunde erneut, um Abweichungen zu minimieren.

4. **Endlosschleife**:
   - Wartet zwischen den Synchronisationen in 1-Sekunden-Intervallen.

---

## Ablauf
1. Das Programm verbindet den Pico mit dem WLAN.
2. Es synchronisiert die Zeit mit einem NTP-Server.
3. Die Zeit und das Datum werden jede Sekunde auf dem LCD angezeigt.
4. Jede Stunde wird die Zeit neu synchronisiert.

---

## Erweiterungsmöglichkeiten
- **Sommerzeit-Unterstützung**:
  - Der `TZ_OFFSET` könnte dynamisch angepasst werden, um Sommerzeit zu berücksichtigen.
- **Fehlerbehandlung**:
  - Verbesserte Behandlung von WLAN- und NTP-Fehlern.
- **Batteriepufferung**:
  - Hinzufügen eines RTC-Moduls (Real Time Clock), um die Uhrzeit
  auch ohne ständige Internetverbindung beizubehalten.

---

## Hardware-Voraussetzungen
1. Raspberry Pi Pico W.
2. I2C-fähiges LCD-Display mit 16x2 Zeichen.
3. WLAN-Netzwerk mit den Zugangsdaten in der Datei `Zugang_DC.py`.

"""


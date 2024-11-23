#==========================================================================
#
# PB-5-4-10-ElKo-Pico W als schnurloser Taster.py
#
# 1 Taster
#
#==========================================================================
#
# Bibliotheken laden
from DCpriv import DCwlanSSID, DCwlanPW
import machine
import network
import rp2
import utime as time
import urequests as requests

# WLAN-Konfiguration
wlanSSID = DCwlanSSID()
wlanPW = DCwlanPW()
#wlanSSID = 'WLANNAME'
#wlanPW = 'WLANPASSWORD'
rp2.country('DE')

# IoT-Webservice-Konfiguration
myID = '691a1f3cda31c9924dac2dc11cff97ad' # 32-stelliger Code
# http://elektronik.info/691a1f3cda31c9924dac2dc11cff97ad
# http://elektronik.info
myDevice = 'demo' # oder selbst gewählter Name
myValue = 1 # Default-Wert

# Status-LED für die WLAN-Verbindung
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
            print('.')
            time.sleep(1)
    if wlan.isconnected():
        print('WLAN-Verbindung hergestellt / WLAN-Status:', wlan.status())
        led_onboard.on()
    else:
        print('Keine WLAN-Verbindung')
        led_onboard.off()
        print('WLAN-Status:', wlan.status())

# WLAN-Verbindung herstellen
wlanConnect()

# Button initialisieren
btn = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
print()
print('Taster bereit')

# Funktion zur Taster-Auswertung
while True:
    time.sleep_ms(100)
    if btn.value() == 0:
        print()
        try:
            if myValue == 0: myValue = 1
            elif myValue == 1: myValue = 0
            url = 'http://elektronik.info/' + myID + '/' + myDevice + '/' + str(myValue)
            # HTTP-Request senden
            print('Request: GET', url)
            response = requests.get(url)
            if response.status_code == 200:
                print('Response:', response.content)
            else:
                print('Status-Code:', response.status_code)
                print('Fehler:', response.reason)
            response.close()
        except OSError:
            print('Fehler: Keine Verbindung')
        # Entprell-Pause
        time.sleep_ms(100)
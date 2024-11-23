#==========================================================================
#
# PB-5-5-10-ElKo-Pico W Sensor-Daten per E-Mail senden.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
import machine
import network
import rp2
import utime as time
import umail
from DCpriv import DCwlanSSID, DCwlanPW, DCmailPW
import umail

# WLAN-Konfiguration
wlanSSID = DCwlanSSID()
wlanPW = DCwlanPW()
#wlanSSID = 'WLANNAME'
#wlanPW = 'WLANPASSWORD'
rp2.country('DE')

# E-Mail-Konfiguration (Sender)
smtpHost = 'smtp.1und1.de'                # ANPASSEN
smtpPort = 587   #25
fromName = 'Temperatur-Sensor'
fromMail = 'dieter.carbon@comidio.de'     # ANPASSEN
fromPW = DCmailPW()

# E-Mail-Konfiguration (Empfänger)
toName = 'Dieter Carbon'
#toMail = 'dieter.carbon@comidio.de'
toMail = (['dieter.carbon@comidio.de', 'john.tracker@gmx.de'])

# E-Mail: Betreff und Text
mailSubject = 'E-Mail von Raspberry Pi Pico W'
mailText = "\n" + 'Diese E-Mail wurde von einem Raspberry Pi Pico W verschickt.'

# Status-LED für die WLAN-Verbindung
led_onboard = machine.Pin('LED', machine.Pin.OUT, value=0)

# Initialisierung des Sensors
sensor_temp = machine.ADC(4)

# Funktion: Temperatur abrufen und umrechnen
def getTemp():
    read = sensor_temp.read_u16()
    spannung = read * 3.3 / (65535)
    temperatur = 27 - (spannung - 0.706) / 0.001721
    return str(temperatur)

# WLAN-Verbindung herstellen
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

# WLAN-Verbindung prüfen
if wlan.isconnected():
    print('WLAN-Verbindung hergestellt / WLAN-Status:', wlan.status())
    led_onboard.on()
    ipconfig = wlan.ifconfig()
    print('IPv4-Adresse:', ipconfig[0])
else:
    led_onboard.off()
    print('WLAN-Status:', wlan.status())
    raise RuntimeError('Keine WLAN-Verbindung')

# Wiederholung (Endlos-Schleife)
while True:
    # Variablen leeren
    tempLog = ()
    temp = ''
    # Alle 3 Minuten einen Sensor-Wert lesen und loggen
    for i in range(3):
        print('Sensor lesen')
        # Temperatur lesen und loggen
        tempLog += (getTemp(),)
        time.sleep(10)
    # Nach 9 Minuten eine E-Mail schicken
    c = len(tempLog)
    for i in range (c): temp += tempLog[i] + "\n"
    print('E-Mail senden')
    smtp = umail.SMTP(smtpHost, smtpPort)
    smtp.login(fromMail, fromPW)
    smtp.to(toMail)
    smtp.write('From: ' + fromName + ' <' + fromMail + '>' + "\r\n")
    smtp.write('To: Dieter Carbon <dieter.carbon@comidio.de>, John Tracker <john.tracker@gmx.de>' + "\r\n")
    smtp.write('Subject: ' + mailSubject + "\r\n\r\n")
    smtp.write(temp + mailText + "\r\n")
    smtp.send()
    smtp.quit()
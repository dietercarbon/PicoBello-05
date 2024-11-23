import network
import socket
import time
import ubinascii
from DCpriv import DCwlanSSID, DCwlanPW, DCmailPW

ssid = DCwlanSSID()
password = DCwlanPW()

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)

    while not wlan.isconnected():
        print("Verbinde mit WLAN...")
        time.sleep(1)

    print("Verbunden mit WLAN")
    print("IP-Adresse:", wlan.ifconfig()[0])

def read_temperature():
    return 23.5

def send_email(subject, body):
    smtp_server = 'smtp.1und1.de'
    smtp_port = 25  # Verwende Port 587 für STARTTLS
    smtp_user = 'dieter.carbon@comidio.de'
    smtp_pass = DCmailPW()

    from_addr = 'dieter.carbon@comidio.de'
    to_addr = 'dieter.carbon@comidio.de'

    msg = f"""\
From: {from_addr}
To: {to_addr}
Subject: {subject}

{body}
"""

    try:
        print("starte try")
        s = socket.socket()
        s.connect((smtp_server, smtp_port))
        print("46")

        # Start der SMTP-Kommunikation
        s.sendall(b"EHLO example.com\r\n")
        response = s.recv(1024)
        print(response.decode())

        # Authentifizierung
        s.sendall(b"AUTH LOGIN\r\n")
        s.sendall(ubinascii.b2a_base64(smtp_user.encode()).strip() + b"\r\n")
        s.sendall(ubinascii.b2a_base64(smtp_pass.encode()).strip() + b"\r\n")

        response = s.recv(1024)
        print(response.decode())

        s.sendall(f"MAIL FROM:<{from_addr}>\r\n".encode())
        response = s.recv(1024)
        print(response.decode())

        s.sendall(f"RCPT TO:<{to_addr}>\r\n".encode())
        response = s.recv(1024)
        print(response.decode())

        s.sendall(b"DATA\r\n")
        response = s.recv(1024)
        print(response.decode())

        s.sendall(msg.encode())
        s.sendall(b"\r\n.\r\n")
        response = s.recv(1024)
        print(response.decode())

        s.sendall(b"QUIT\r\n")
        response = s.recv(1024)
        print(response.decode())

        s.close()
        print("E-Mail erfolgreich gesendet")
    except Exception as e:
        print("Fehler beim Senden der E-Mail:", e)

connect_wifi()

while True:
    temp = read_temperature()
    subject = "Temperaturdaten"
    body = f"Die aktuelle Temperatur beträgt {temp} °C."
    send_email(subject, body)
    time.sleep(10)  # Warte eine Stunde bis zur nächsten Messung

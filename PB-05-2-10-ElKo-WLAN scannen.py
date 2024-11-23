#==========================================================================
#
# PB-05-2-10-ElKo-WLAN scannen.py
#
# (keine Bauteile)
#
#==========================================================================
#
# Bibliotheken laden
import network

# Client-Betrieb
wlan = network.WLAN(network.STA_IF)

# WLAN-Interface aktivieren
wlan.active(True)

# WLANs ausgeben
print(wlan.scan())

"""
Das obige Python-Programm enthält Code zum Scannen und Auswerten von WLAN-Netzwerken.
Hier wird zunächst die Bibliothek "network" importiert. Anschließend wird ein WLAN-Client gestartet
und das WLAN-Interface aktiviert.

Mit der Funktion "wlan.scan()" wird eine Liste von verfügbaren WLAN-Netzwerken erstellt. Die
Ergebnisse des WLAN-Scans werden als Liste von Tupeln zurückgegeben. Jedes Tupel enthält
Informationen zu einem gefundenen WLAN-Netzwerk, wie z.B. den Namen (SSID), die
MAC-Adresse, den Signalpegel (RSSI) und die Verschlüsselungsmethode.

Der Befehl "print(wlan.scan())" gibt die Ergebnisse des WLAN-Scans auf der Konsole aus,
was dem Benutzer ermöglicht, die verfügbaren WLAN-Netzwerke zu sehen und zu analysieren.


>>> %Run -c $EDITOR_CONTENT
[(b'Blackbox Gastzugang', b'\xf2\xb0\x14\x9bUi', 1, -70, 5, 3),
(b'Blackbox', b'\xf0\xb0\x14\x9bUi', 1, -73, 5, 2),
(b'Blackbox', b'\xe8\xdfp\x1du\x1d', 1, -90, 5, 1),
(b'TP-Link', b'\xac\x15\xa2\x1b\x80\xa6', 5, -65, 7, 9),
(b'Blackbox', b'|\xffM\xfc\x07\x8c', 6, -84, 5, 3),
(b'Blackbox Gastzugang', b'~\xffM\xfc\x07\x8c', 6, -89, 5, 2),
(b'Johanna2', b'\xdc9oB\x14\xcf', 11, -56, 5, 4),
(b'Blackbox', b'\xdc9o\x82*\x9b', 11, -85, 5, 2),
(b'Johanna2', b'\x98\x9b\xcb\xad\xa3\x99', 11, -69, 5, 2),
(b'Blackbox Gastzugang', b'\xde9o\x82*\x9b', 11, -86, 5, 2)]
>>>

Bitte erkläre anhand von " (b'TP-Link', b'\xac\x15\xa2\x1b\x80\xa6', 5, -65, 7, 9)"
detailliert jeden enzelnen Ausgabe-Parameter mit Name, Bedeutung und Bewertung
ChatGPT

Gerne erkläre ich jeden einzelnen Ausgabe-Parameter der WLAN-Scan-Ergebnisse:

    Name (b'TP-Link'):
        Bedeutung: Dies ist der Name des WLAN-Netzwerks (SSID), wie es in den
        Einstellungen des Routers oder Access Points festgelegt wurde.
        Bewertung: Der Name gibt Hinweise auf den Netzwerkadministrator oder
        das Modell des Routers/Access Points. Es ist ein wichtiger Identifikator
        für das WLAN-Netzwerk, um sich mit ihm zu verbinden.

    MAC-Adresse (b'\xac\x15\xa2\x1b\x80\xa6'):
        Bedeutung: Die MAC-Adresse (Media Access Control-Adresse) ist eine eindeutige
        Kennung, die jedem Netzwerkgerät zugewiesen ist. Sie dient dazu, Geräte
        in einem Netzwerk zu identifizieren.
        Bewertung: Die MAC-Adresse wird normalerweise nicht direkt vom Benutzer
        verwendet. Sie ist jedoch hilfreich für Netzwerkadministratoren, um Geräte
        zu identifizieren und sicherzustellen, dass nur bekannte Geräte
        auf das Netzwerk zugreifen.

    Kanal (5):
        Bedeutung: Der Kanal ist die Funkfrequenz, auf der das WLAN-Netzwerk
        betrieben wird. In den meisten Regionen gibt es mehrere Kanäle,
        die für WLAN genutzt werden können.
        Bewertung: Ein niedriger Kanalwert kann auf eine Überlastung oder Interferenz
        hindeuten, während ein höherer Kanalwert normalerweise weniger Störungen bedeutet.

    Signalstärke (-65):
        Bedeutung: Die Signalstärke oder Signalqualität gibt an, wie stark das
        WLAN-Signal an der Position des Scanners empfangen wird. Sie wird
        in Dezibel Milliwatt (dBm) gemessen.
        Bewertung: Je höher die Signalstärke (in Richtung 0 dBm), desto besser ist
        die Verbindung. Ein Wert wie -65 dBm ist in der Regel ein ziemlich guter
        Signalwert und deutet auf eine relativ nahegelegene Quelle hin.

    Verschlüsselungstyp (7):
        Bedeutung: Dieser Parameter zeigt den verwendeten Verschlüsselungstyp
        für das WLAN-Netzwerk an. Unterschiedliche Zahlen entsprechen verschiedenen
        Verschlüsselungsprotokollen.
        Bewertung: Eine Verschlüsselung, z. B. WPA2, ist wichtig für die Sicherheit
        des WLAN-Netzwerks, da sie verhindert, dass unbefugte Personen auf das Netzwerk
        zugreifen und Daten abfangen können.

    Authentifizierung (9):
        Bedeutung: Die Authentifizierungsmethode gibt an, wie Geräte sich beim
        WLAN-Netzwerk anmelden, um Zugriff zu erhalten. Verschiedene Zahlen
        entsprechen unterschiedlichen Authentifizierungsverfahren.
        Bewertung: Die Authentifizierung ist eine weitere Sicherheitsebene und kann
        z. B. WPA2-Personal (PSK) oder WPA2-Enterprise (EAP) umfassen.

Zusammenfassend bietet das WLAN-Scan-Ergebnis die Informationen über die verfügbaren
WLAN-Netzwerke in der Umgebung, einschließlich ihrer Namen, Signalstärken,
Verschlüsselungstypen und Authentifizierungsmethoden. Die Informationen sind nützlich,
um das geeignetste WLAN-Netzwerk für die Verbindung auszuwählen und eine sichere
Verbindung herzustellen.


Interpretation:

    Kanäle im Bereich von 1 bis 11 deuten normalerweise auf 2,4 GHz WLAN hin.
    Kanäle im Bereich von 36 bis 165 deuten normalerweise auf 5 GHz WLAN hin.

Da der Kanal des WLANs mit dem Namen "TP-Link" den Wert "5" hat, handelt es sich
vermutlich um ein 2,4 GHz WLAN.

"""
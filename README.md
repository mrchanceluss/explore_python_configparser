# python - Credentials nutzen mit configparser
Neulich benötigte ich für meine ersten Experimente mit couchDB Administrator-Credentials um eine Datenbank zu erzeugen. Ich wollte unbedingt Nutzernamen und Passwort als Klartext im Quellcode vermeiden.
Bei meiner Suche nach einer soliden und gleichzeitig einfachen Lösung bin ich dem configparser auf python.org begegnet ([Link](docs.python.org/3/library/configparser.html)).

##  Eine ini-Datei anlegen
Mit configparser lassen sich einfach strukturierte Einstellungsdateien nutzen. In einem Verzeichnis unserer Wahl legen wir eine Datei namens credentials.ini an und die schreiben die benötigten Anmeldedaten hinein.

    [couchdb_admin]
    user = admin
    password = yourpassword

    [couchdb_user]
    user = Tom
    password = hispassword

In den eckigen Klammern steht die Section. Sie ist, einfach gesagt, der frei wählbare Bezeichner für die darunter stehenden Daten. Anhand dieses Bezeichners finden wir später die für uns relevanten Daten. Die Einträge in jeder Section folgen dem key-value-pair-Schema. Auf diese Art können wir verschiedenste Daten speichern, nicht nur Anmeldedaten. Welchen Datensatz wir verwenden wollen teilen wir dem configparser mit.

## Das python-Skript

Um unsere Daten aus der zuvor erstellten ini-Datei auslesen zu können, wird als Erstes das Modul configparser importiert. 

    import configparser

Dann erzeugen wir ein *configparser-Objekt* namens config und lesen unsere *credentials.ini* ein.

    config = configparser.ConfigParser()
    config.read('credentials.ini')

In unserem config befinden sich jetzt alle Einträge aus der ini-Datei. Wir greifen nun auf den Datensatz couchdb_admin zu und speichern ihn in der Variable credentials. 

    print(credentials['user']) print(credentials['password'])

Und zu guter Letzt hier nochmal der gesamt Code in der Übersicht.

    import configparser

    config = configparser.ConfigParser()config.read('credentials.ini')
    credentials = config['couchdb_admin']

    print(credentials['user']) print(credentials['password'])

## Wozu das alles?
Für mich als python-noob ist es zunächst einmal eine gute Fingerübung zum Umgang mit externen, menschenlesbaren Konfigurationsdateien. Die Anwendung ist nicht auf Login-Daten beschränkt, vielleicht is es nicht einmal die beste Lösung dafür. Momentan ist es jedoch ausreichend.
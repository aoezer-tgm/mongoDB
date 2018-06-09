#Uebungen zu MongoDB
Grundkompetenz

    Erstelle eine mongodb - Datenbank mit einer Collection students, die Datensaetze in folgendem Format hat

    { "name":"Schueler 1", "jahr":"2000", "klasse": "4xhit", "ampeln":[{"fach":"AM","farbe":"gelb"},{"fach":"INSY","farbe":"gruen"},...] }

    Erstelle ein  Programm, das sich zu der Datenbank verbindet und fuenf neue Schueler (mit verschiedenen Daten) in die students-Collection im richtigen Format hinzufuegt. (Zugriff von Python: [1], Dokumentation zu inserts: [2] )

    Fuehre folgende Abfragen durch:
    - Alle Schueler
    - Alle Schueler, die 2000 gebohren sind
    - Alle Schueler, die 2000 gebohren sind, oder aelter
    - Alle Schueler, die 2000 geboren sind und in die Klasse 4dhit gehen
    - Alle Schueler, die in die Klasse 4dhit gehen und in "AM" eine rote Ampel haben
    (Dokumentation zu Such-Operatoren: [3])

Erweiterte Kompetenz

    Fuehre folgende Abfragen mittels MapReduce durch:
    - Gib fuer jede Klasse die durchschnittliche Anzahl an roten Ampeln in AM aus
    - Gib fuer jede Ampelfarbe an, wie oft sie in der Klasse 5ahit aufgetreten ist (Hinweise: man kann die emit()-Methode auch mehrfach in einem reduce-Vorgang aufrufen)

    Recherche - Aufgabe: Wie konfiguriert man MongoDB zum Betrieb in einem Cluster (a) als Master/Slave und (b) als Replication Set. Gib die noetigen Konfigurationsoptionen an sowie, wie man sich von einer Anwendung zum Cluster verbindet.

Abgabe

- als Protokoll (PDF) inklusive sourcecodes, Beispieldaten, und Erklaerungen

1. https://api.mongodb.com/python/current/tutorial.html

2. https://docs.mongodb.com/manual/tutorial/insert-documents/

3. https://docs.mongodb.com/manual/tutorial/query-documents/ 
 
 bzw die dort unter "Additional Query Tutorials" verlinkten Seiten
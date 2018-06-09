from random import randint
from pymongo import MongoClient
from pymongo import InsertOne, DeleteMany, ReplaceOne, UpdateOne
import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)

# Verbindungsaufbau zur Datenbank
db = client['schueler-database']
col = db['schueler_collection']


post = { "name":"Schueler 1", "jahr":"2000", "klasse": "4xhit", "ampeln":[{"fach":"AM","farbe":"gelb"},{"fach":"INSY","farbe":"gruen"}] }

posts = db.schueler
post_id = posts.insert_one(post).inserted_id
post_id

pprint.pprint(posts.find_one())

db.schueler_collection.delete_many({})

db.schueler_collection.insert_many([
            {"name": "Schueler 1", "jahr": "1999", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 2", "jahr": "2000", "klasse": "4dhit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 3", "jahr": "2001", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 4", "jahr": "2002", "klasse": "4dhit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 5", "jahr": "2003", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 6", "jahr": "1956", "klasse": "4dhit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 7", "jahr": "1945", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 8", "jahr": "1939", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 9", "jahr": "1999", "klasse": "4chit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 10", "jahr": "2000", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 11", "jahr": "2001", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 12", "jahr": "2002", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 13", "jahr": "2003", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 14", "jahr": "1956", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 15", "jahr": "1945", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "rot"}, {"fach": "INSY", "farbe": "gruen"}]},
            {"name": "Schueler 16", "jahr": "1939", "klasse": "5ahit","ampeln": [{"fach": "AM", "farbe": "gelb"}, {"fach": "INSY", "farbe": "gruen"}]}
        ])

all = db.schueler_collection.find( {} )

geboren2000 = db.schueler_collection.find({"jahr": "2000"})

geboreb2000groe = db.schueler_collection.find({"$or": [{"jahr": "2000"}, {"jahr": {"$gt": "2000"}}]})

geboren20004d = db.schueler_collection.find({"jahr": "2000", "klasse":"4dhit"})

ampel = db.schueler_collection.find({"klasse":"4dhit", "ampeln.fach":"AM", "ampeln.farbe":"rot"})

rot4d = db.schueler_collection.find({"klasse":"4dhit","ampeln.fach":"AM", "ampeln.farbe":"rot"}).count()
alle4d = db.schueler_collection.find({"klasse":"4dhit"}).count()

rot4c = db.schueler_collection.find({"klasse":"4chit","ampeln.fach":"AM", "ampeln.farbe":"rot"}).count()
alle4c = db.schueler_collection.find({"klasse":"4chit"}).count()

gruen5a = db.schueler_collection.find({ "klasse":"5ahit","ampeln.farbe":"gruen"}).count()
gelb5a = db.schueler_collection.find({ "klasse":"5ahit","ampeln.farbe":"gelb"}).count()
rot5a = db.schueler_collection.find({ "klasse":"5ahit","ampeln.farbe":"rot"}).count()
alle5a = db.schueler_collection.find({"klasse":"5ahit"}).count()



print("Alle Schueler")
for sel in all:
  print(sel)
print()
print("Alle Schueler, die 2000 gebohren sind")
for sel in geboren2000:
    print(sel)
print()
print("Alle Schueler, die 2000 gebohren sind, oder aelter")
for sel in geboreb2000groe:
    print(sel)
print()
print("Alle Schueler, die 2000 geboren sind und in die Klasse 4dhit gehen")
for sel in geboren20004d:
    print(sel)
print()
print("Alle Schueler, die in die Klasse 4dhit gehen und in 'AM' eine rote Ampel haben")
for sel in ampel:
    print(sel)
print()
print("Gib fuer jede Klasse die durchschnittliche Anzahl an roten Ampeln in AM aus")
print(str(int(rot4d/alle4d*100))+" prozent für die 4d")
print(str(int(rot4c/alle4c*100))+" prozent für die 4C")
print(str(int(rot5a/alle5a*100))+" prozent für die 5a")
print()
print("Gib fuer jede Ampelfarbe an, wie oft sie in der Klasse 5ahit aufgetreten ist")
print(str(int(gruen5a))+" Grüne")
print(str(int(gelb5a))+" Gelbe")
print(str(int(rot5a))+" Rote")

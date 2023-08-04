
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os 
from pathlib import Path
from prettytable import PrettyTable
import inoutput as io

os.chdir(Path(__file__).parent)

cred = credentials.Certificate("grapefruit256-27d68-f431ea3c7ed1.json")


dbEnd = True
try:
    firebase_admin.initialize_app(cred)
except ValueError as e:
    print(f"Initialisation Check of service account: {e}")
    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
    #print("try1 - raise ValueError",dbEnd)


try:
    token = cred.get_access_token().access_token  # Abrufen des Access Tokens
    if token:  # Wenn kein Token gefunden wird, ist das Zertifikat ungültig
        raise ValueError('Service account certificate valid - no new pentis version required')
    
    #print("try2 - token - raise ValueError", dbEnd)

except ValueError as e:
    print(f"Checking service account: {e}")
    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
except Exception as e:
    print(f"Service account certificate not valid anymore - new pentis version download required: {e}")
    dbEnd = False
    #print("newVersion:", dbEnd)

    # Hier können Sie Ihre Fehlerbehandlung durchführen, z.B. das Programm beenden oder eine Benachrichtigung senden
#else:
#    print("Der Schlüssel des Firebase-Dienstkontos ist ungültig.")


#app = firebase_admin.initialize_app(cred)
# Zugriff auf firestore
if dbEnd == False:
        io.keyBox()

db = firestore.client()

name = "Norbert Noname"
score = 2057


def addHighscore(name, score):
    scores_ref = db.collection("pentisLab")
    query = scores_ref.where("name", "==", name)
    results = query.get()

    if len(results) > 0:
        for doc in results:
            if doc.to_dict()["score"] >= score:
                print(f"{name} is already in the collection with a higher score.")
            else:
                doc.reference.update({"score": score})
                print(f"{name} has been updated with the new score.")
    else:
        scores_ref.add({
            "name": name,
            "score": score
        })
        print(f"{name} has been added to the collection.")
    #return dbEnd


def getHighscores():
    scores = []
    scores_ref = db.collection("pentisLab")
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(10)
    for doc in query.stream():
        scores.append(doc.to_dict())
    return scores
def getHighscores20():
    scores = []
    scores_ref = db.collection("pentisLab")
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(20)
    for doc in query.stream():
        scores.append(doc.to_dict())
    return scores

def clearHighscores():
    scores_ref = db.collection("pentis_scores")
    docs = scores_ref.stream()
    for doc in docs:
        doc.reference.delete()


def printHighscores():
    scores = []
    scores_ref = db.collection("pentisLab")
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(10)
    for doc in query.stream():
        scores.append(doc.to_dict())
    table = PrettyTable()
    table.field_names = ["Rank", "Name", "Score"]
    table.get_string
    for i, score in enumerate(scores):
        table.add_row([i+1, score["name"], score["score"]])
    #print(table)
    #tableUni = table.get_string().encode('utf-8')
    tableUni = table.get_string()
    return tableUni

def printHighscoresManually():
    i = 0
    scores = []
    scores_ref = db.collection("pentisLab")     # scores_ref = <google.cloud.firestore_v1.collection.CollectionReference object at 0x00000216853A1340>
    query = scores_ref.order_by("score", direction=firestore.Query.DESCENDING).limit(10)
    for doc in query.stream():                  # doc = <google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x00000160173A3E50>
        scores.append(doc.to_dict())
    print("Name" + "\t\t\tScore")
    for i in range(len(scores)):
        print(scores[i]["name"] + "\t\t\t", scores[i]["score"])    
        

#scores = getHighscores()
#print(scores)




#addHighscore(name, score)

#allScores = getHighscores()
#print(allScores)
#print("fbRW: Number 1: ", allScores[0])
#print("fbRW: Last score: ", allScores[-1]["score"])
#clearHighscores()
#allScores = getHighscores()
#print(allScores)

""" rankdata = {"name": "Pete", "score": 111458 }

def writeFunc(data):
    db.collection("pentisLab").document("highscores").set(data)

def readFunc():
    result2 = db.collection("pentisLab").document("highscores").get()
    print(result2.to_dict()) """

    
#writeFunc(rankdata)
#readFunc()



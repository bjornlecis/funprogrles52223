punten = {"bert":9,"jan":7,"hanne":8}

def voeg_punt_toe():
    naam = input("geef de naam in")
    punt = int(input("geef het punt"))
    #punten.update({naam:punt}) optie 1
    punten[naam] = punt # optie 2

def verwijder_punt():
    naam = input("welke naam en punt wil je verwijderen")
    punten.pop(naam)

voeg_punt_toe()
verwijder_punt()
for punt in punten.values():
    print(punt)

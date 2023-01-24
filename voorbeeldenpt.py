from prettytable import PrettyTable

#voorbeeld 1
punten = [8,3,8,5,2]
tabel_punten = PrettyTable(["punten"])
for punt in punten:
    tabel_punten.add_row((str(punt)))
print(tabel_punten)

#voorbeeld 2
punten_leerlingen={"Mario":9,"Luigi":7,"Peach":10,"Yoshi":6,"Browser":4}
tabel_punten_leerlingen = PrettyTable(["Naam","Punten op 10"])
for leerling,punt in punten_leerlingen.items():
    tabel_punten_leerlingen.add_row([leerling,str(punt)])
print(tabel_punten_leerlingen)

#voorbeeld update
naam_leerling = input("leerling naam")
punt_lln = input("geef de punten in")
#tabel_punten_leerlingen.add_row([naam_leerling,punt_lln])
print(tabel_punten_leerlingen)



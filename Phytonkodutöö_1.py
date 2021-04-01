# Karin Leht-Järv ITT20

#Tervitus
print ("Tere, maailm!")

#Aasta liblikas

aasta = 2020
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = ".aasta liblikas on "
lause = str(aasta)+lause_keskosa+liblikas
print(lause)

#Astendamine

alus = int(input("Sisestage astme alus: "))
astendaja = int(input("Sisestage astendaja: "))
aste = alus**astendaja
print(aste)

#Trahv

nimi = input("Sisestage oma nimi: ")
lubatud_kiirus = int(input("Sisestage lubatud kiirus (km/h): "))
tegelik_kiirus = int(input("Sisestage tegelik kiirus (km/h): "))
trahv = min(190,(tegelik_kiirus-lubatud_kiirus)*3)
print(nimi+", kiiruse ületamise eest on teie trahv",trahv,"eurot")
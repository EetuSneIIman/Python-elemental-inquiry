
# ProjektiTyö 2


# Avataan ja luetaan tiedosto.
Oikeat = open("D:\\koulupython\\alkuaineet.txt", "r")

muuttuja2 = Oikeat.read().splitlines()

# Alkutekstit ja ohjeet.

print("Tervetuloa! ")
print(" ")
print("Tehtävänä on sanoa ensimmäisestä kahdestakymmenestä alkuaineesta viisi. ")
print(" ")

# Listat

Arvosanat = ["Kaikki väärin, yritä uudelleen. ", "Huono. ",
             "Keskitasoa huonompi. ", "Keskitasoa parempi. ", "Loistavaa. ", "Täydellistä. "]
OVastaukset = []
VVastaukset = []
EVastaukset = []
kaikkivastaukset = []

# Kysymys funktio.


def kysymys():
    vastaus = input("Anna vastaus: ")
    vastaus = vastaus.lower()

    if vastaus.isalpha() == False:
        print("Epäsopiva vastaus. ")
        EVastaukset.append(vastaus)
        kysymys()

    elif vastaus in kaikkivastaukset:

        print("Ei duplikaatteja! ")
        kysymys()

    else:
        if vastaus in muuttuja2:
            OVastaukset.append(vastaus)

        else:
            VVastaukset.append(vastaus)

    kaikkivastaukset.append(vastaus)

# Kutsutaan funktio viisi kertaa.


while True:

    kysymys()
    kysymys()
    kysymys()
    kysymys()
    kysymys()

    break

# Tulostetaan oikeiden vastausten määrä ja arvosana.

if len(OVastaukset) == 1:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("20%")
    print(Arvosanat[1])

if len(OVastaukset) == 2:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("40%")
    print(Arvosanat[2])

if len(OVastaukset) == 0:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("0%")
    print(Arvosanat[0])

if len(OVastaukset) == 3:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("60%")
    print(Arvosanat[3])

if len(OVastaukset) == 4:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("80%")
    print(Arvosanat[4])

if len(OVastaukset) == 5:
    print(" ")
    print("Oikeiden vastausten määrä: ")
    print("100%")
    print(Arvosanat[5])

print(" ")
print("Oikeat vastaukset")
print(OVastaukset)
print(" ")

print("Väärät vastaukset")
print(VVastaukset)
print(" ")

print("Kaikki vastaukset")
print(kaikkivastaukset)
print(" ")
print("Kiitos kun käytit ohjelmaa. ")


Oikeat.close()

# EOF

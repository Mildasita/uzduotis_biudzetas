# Patobulinti 5 pamokos biudzeto programa:
# • Sukurti tévine klase Irasas, kurioje bütu savybes suma, is kurios klasés PajamuIrasas ir IslaiduIrasas 
# paveldétu visas savybes. +
# • I klase PajamuIrasas papildomai pridéti savybes siuntejas ir papildoma_informacija, kurias vartotojas galétu
#  irasyti. +
# • I klase IslaiduIrasas papildomai pridéti savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias 
# vartotojas galétu irasyti. +
# • Atitinkamai perdaryti klases Biudzetas metodus gauti_balansa ir gauti_ataskaita kad pasiemus irasa is 
# zurnalo, atpazintu, ar tai yra pajamos ar islaidos (pvz., panaudojus isinstance() metoda) ir atitinkamai 
# atliktu veiksmus.
# • Padaryti, kad vartotojui (per konsole) bütu leidziama irasyti pajamu ir islaidu irasus, perziuréti 
# balansa ir ataskaita.


import pickle

FILE_NAME = "biudzetas.pkl"

class Irasas:
    def __init__(self, tipas, suma):    
        self.tipas = tipas                                       # finansai = pajamos ar islaidos
        self.suma = suma              

    def __str__(self):                                                   # prisidedam __str__ metoda, grazina objekto teksta.
        return f"{self.tipas}: {self.suma} EUR"                        # pvz. "pajamos: 100 eur"
    
class PajamuIrasas(Irasas): 
    tipas = "Pajamos"                                            # su "Pajamos" nusirodom finansai kokia
    def __init__(self, suma, siuntejas, papildoma_informacija):           #  I klase PajamuIrasas papildomai pridéti 
        super().__init__(self.tipas, suma)                                 # savybes siuntejas ir papildoma_informacija, 
        self.siuntejas = siuntejas                                         # kurias vartotojas galétu irasyti.
        self.papildoma_informacija = papildoma_informacija                


    def __str__(self):                                                      # atsiprintinam pajamu info (kiek, is kur gauta, papil.info)
        return f"{self.tipas}: {self.suma} EUR, Siuntėjas: {self.siuntejas}, Info: {self.papildoma_informacija}"


class IslaiduIrasas(Irasas):
    tipas = "Islaidos"
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):   #I klase IslaiduIrasas papildomai pridéti 
        super().__init__(self.tipas, suma)                                  #savybes atsiskaitymo_budas ir isigyta_preke_paslauga, kurias 
        self.atsiskaitymo_budas = atsiskaitymo_budas                        # kurias, vartotojas galétu irasyti. +
        self.isigyta_preke_paslauga = isigyta_preke_paslauga


    def __str__(self):                                                      # atsiprintinam islaidu info (kiek, kaip, uz ka)
        return f"{self.tipas}: {self.suma} EUR, Būdas: {self.atsiskaitymo_budas}, Prekė/Paslauga: {self.isigyta_preke_paslauga}"


class Biudzetas:
    def __init__(self):   
        self.zurnalas = []                                                 # susikuriam zurnala, kur matysis visos pajamos ir islaidos


    def prideti_pajamu_isras (self, suma, siuntejas, papildoma_informacija):   
        irasas = PajamuIrasas (suma, siuntejas, papildoma_informacija)
        self.zurnalas.append(irasas)

    def prideti_islaidos_isras (self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        irasas = IslaiduIrasas (suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        self.zurnalas.append(irasas)

    def gauti_balansa(self):            # susiskaiciuojam visas pajamas(isl) is zurnalo,pereinam su isinstance per classe, jei pajamos isitraukiam i suma
        pajamos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, PajamuIrasas))
        islaidos = sum(irasas.suma for irasas in self.zurnalas if isinstance(irasas, IslaiduIrasas))
        return pajamos - islaidos

    def parodyti_ataskaita(self):               # atsprintinan ataskaita (irasu zurnala)
        for irasas in self.zurnalas:   
            print(irasas)


try:
    with open(FILE_NAME, "rb") as f:         #isikeliam senus duomenis
      biudzetas = pickle.load(f)
except FileNotFoundError:
      biudzetas = Biudzetas()                  # Jei failo nėra, pradedame su tuščiu sąrašu

def issaugoti_duomenis(biudzetas):
      with open(FILE_NAME, "wb") as f:            # issisaugom ivestus duomenis i failiuka
          pickle.dump(biudzetas, f)

while True:
    print("******** BIUDZETAS ***")
    print("1 - Pridėti pajamas")
    print("2 - Pridėti išlaidas")
    print("3 - Pajamu ir islaidu balansas")
    print("4 - Parodyti ataskaita")
    print("5 - Išeiti")

    pasirinkimas = input("Pasirinkite veiksmą: ")

    if pasirinkimas == "1":
        suma = float(input("Ivesti pajamu suma: "))
        siuntejas = input("Ivesti siunteja: ")
        papildoma_informacija = input("Ivesti papildoma info: ")
        biudzetas.prideti_pajamu_isras(suma, siuntejas, papildoma_informacija)   #susidedam pajamas i biudzeto zurnala
        issaugoti_duomenis(biudzetas)                                             # issisaugom i agurkeli 
    elif pasirinkimas == "2":
        suma = float(input("Ivesti islaidu suma: "))
        atsiskaitymo_budas = input("Atsiskaitymo budas: ")
        isigyta_preke_paslauga = input("Isigyta preke/paslauga: ")
        biudzetas.prideti_islaidos_isras(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
        issaugoti_duomenis(biudzetas)
    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.gauti_balansa()} EUR")                   #atsiprintinam biudzeta
    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()                                        # atsiprintinam ataskaita
    elif pasirinkimas == "5":
        print("Programa baigta.")                                             # susinaikinam
        break
    else:
        print("Neteisingas pasirinkimas, bandykite dar kartą.")

    print("\n")
# Titel: Periodiska Systemet
# Uppgiftsnummer: 178
# Författare: Sara Wahlqvist
# Datum: 2024-12-08
# Detta program kan änvändas för att träna på det periodiska systemet
# Användaren kan välja mellan att visa en lista av alla atomer i det periodiska systemet, alternativt att förhöra sig själv på atomnummer eller atombeteckningar
# Programmet har inhämtat atombeteckningar och atommassor från filen 'https://www.csc.kth.se/~marko/P/avikt.txt' samt atomnamn från 'https://www.csc.kth.se/~lk/P/avikt.txt' som
# tillhandahållits av kurslärare 
# Datastrukturer: lista vid namn 'atomer' i vilken objekt av klassen atom lagras

import random

#import keyboard
#Denna modul hade jag tänkt att implementera inför slutredovisningen. Jag vill att användaren ska kunna fortsätta generera frågor av önskad sort genom att trycka på enter
#och kunna välja när den vill återgå till huvudmenyn, då via esc.)

class Atom:
    '''Klass som beskriver en atom
       atombeteckning - förkortning av atomnamn, av datatypen sträng
       atomvikt - atomens vikt, av datatypen flyttal
       atomnamn - atomens fullständiga namn, av datatypen sträng
       atomnummer - atomens nummer och därav placering i periodiska systemet, av datatypen heltal'''
    
#Metoder
    def __init__(self, atombeteckning, atomnummer, atomnamn, atomvikt):
        '''Skapar en ny atom
           Inparametrar: self, atombeteckning (str), atomnummer(int), atomnamn (str), atomvikt(float)'''
        self.beteckning = atombeteckning
        self.nummer = atomnummer
        self.namn = atomnamn
        self.vikt = atomvikt
       
    def __str__(self):
        '''Returnerar en sträng som representerar atomen.
           Inparameter: self
           Returvärde: - '''
        return str(self.nummer) + " - " + self.beteckning + "   Atomnamn: " + self.namn + "   Atomvikt: " + str(self.vikt)

    def __lt__ (self, other):
        '''Anropas när en lista av objekt av klassen atom sorteras, t.ex. atomer.sort(). Sorterar atomerna i stigande ordning med avseende på atomvikt.
           Inparameter: self, other
           Returvärde: True resp. false beroende på om villkoret uppfylls (bool)'''
        return self.vikt < other.vikt

class periodisktSystem:
    '''Klass som beskriver ett periodiskt system
       atomlista - lista av atom-objekt som utgör det periodiska systemet, av datastrukturen lista'''

#Metoder
    def __init__(self, atomlista):
        '''Skapar ett periodiskt system
        Inparametrar: self, atomlista (lista)'''
        self.atomlista = atomlista

    def visaAtomer(self):
        '''Skriver ut den representerande strängen för varje atom i attributet "atomlista"
           Inparameter: self'''
        self.atomlista.sort(key=lambda atom: atom.nummer)
        for atom in self.atomlista:
            print(atom)
            
    def slumpaAtom(self):
        '''Slumpar fram en atom ur atomlista
           Inparameter: self
           Returvärde: slumpad atom (objekt)'''
        return random.choice(self.atomlista)    
       
#Funktioner
def läsInFrånFil():
    '''Öppnar tillfälligt importfilen och skapar ett nytt objekt av klassen atom för varje rad i filen. Atomernas beteckning, namn och vikt definieras av radens
       samtliga textstycken separerade med " ". Samtliga objekt läggs till i en lista vid namn 'atomer'. Anropar funktionen bestämAtomnummer().
       Inparameter: -
       Returvärde: returvärdet från funktionen bestämAtomnummer(), dvs. atomlista (lista) '''
    with open("avikt.txt","r", encoding="utf-8") as atomfil:
        atomerUtanNummer = []
        for rad in atomfil:
            atombeteckning, atomnamn, atomvikt = rad.strip().split(" ")
            atom = Atom(atombeteckning.strip(), 0 , atomnamn.strip(), float(atomvikt.strip())) #samtliga atomer tilldelas nummer '0' tills atomnumret bestäms
            atomerUtanNummer.append(atom)
        return bestämAtomnummer(atomerUtanNummer)

def bestämAtomnummer(atomlista):
    '''Sorterar atomlistan baserat på atomvikt och byter plats på atomer med följande index: 17 och 18, 26 och 27, 51 och 52, 89 och 90 samt 91 och 92 då ordningen
       för dessa ej följer atomvikten. Sedan tilldelas atomnummer till varje atom baserat på dess placering i listan. Den med lägst atomvikt tilldelas nummer 1 osv. fram
       till nummer 103 (med undantag för ovannämnda nummerpar).
       Inparameter: atomlista (lista)
       Returvärde: atomlista (lista)'''
    atomlista.sort()   
    bytaPlatsPar = [(17, 18), (26, 27), (51, 52), (89, 90), (91, 92)]
    for a,b in bytaPlatsPar:
        atomlista[a], atomlista[b] = atomlista[b], atomlista[a]
    n = 1
    for atom in atomlista:
        atom.nummer = n
        n += 1
    return atomlista
        

def skrivUtHuvudmeny():
    '''Skriver ut huvudmenyn som består av 4 valmöjligheter
       Inparameter: -
       Returvärde: användar-input (menyval) av datatypen sträng'''
    print("HUVUDMENY:\n","1) Visa en lista av alla atomer i det periodiska systemet\n", "2) Träna på atomnummer\n", "3) Träna på atombeteckningar\n", "4) Avsluta\n")
    return input("Vad vill du göra?: ")

def väljaÖvningsmetod(attributSomÖvasOrd, attributSomÖvas, atomensNamn):
    '''Låter användaren välja på vilket sätt den vill förhöra sig själv på, alltså ange atomnummer/atombeteckning för ett givet atomnamn eller genom att ange
       atomnamnet för ett givet atomnummer/atombeteckning. Godtagbar inmatning är 1 eller 2. Annan inmatning tolkas som felaktig vilket leder till att användaren får göra en ny.
       Inparametern 'attributSomÖvasOrd' är ordet på atomegenskapen som övningen går ut på dvs. 'atomnummer' eller 'atombeteckning'. 'attributSomÖvas' är atomnumret eller
       atombeteckningen på den slumpade atomen i fråga och atomensNamn är namnet på denna atom. Jag jobbar på bättre, tydligare namn till dessa inparametrar.'''
    while True:
        vald_övningsmetod = input(f'Hur vill du öva? 1) Ange {attributSomÖvasOrd} för korresponderande atomnamn 2) Ange atomnamn för korresponderande {attributSomÖvasOrd}:')
        if vald_övningsmetod == "1":
            svaraPåFråga(f'har {attributSomÖvasOrd}: ',atomensNamn, attributSomÖvas)
            break
        elif vald_övningsmetod == "2":
            svaraPåFråga(f'är {attributSomÖvasOrd} till (ange atomnamnet): ',attributSomÖvas, atomensNamn)
            break
        else:
            print("Felaktig inmatning. Vänligen ange 1 eller 2 för något av alternativen ovan.")
   

def svaraPåFråga(fråga, atomvärde, svar):
    '''Funktionen ger användaren max tre försök att besvara övningsuppgiften. Efter tre felaktiga försök, alternativt om funktionen ärInmatningRätt returnerar True skickas användaren
       tillbaka till huvudmenyn. 
       Inparametrar: fråga (str), atomvärde(str)), svar(str))'''
    while True:
        for försök in range(3):
            inmatning = input(f'{atomvärde} {fråga}')
            if ärInmatningRätt(inmatning, svar) == True:
                return
        print("Nu är dina tre försök slut. Det rätta svaret var: ", svar)
        break


def ärInmatningRätt(inmatning, svar):
    '''Kontrollerar om användarens inmatning är korrekt. Funktionen gör om inmatningen såväl som svaret till gemener så att användaren kan mata in svaret med stora såväl som
       små bokstäver. 'svar' konverteras till en sträng för att kunna jämföras med inmatning
       Inparametrar: inmatning (str), svar(str)
       Returvärde: om inmatningen är korrekt returneras True (bool)'''
    if inmatning.lower() == str(svar.lower()):
        print("Rätt! Bra.")
        return True
    print("Det var fel. Vänligen försök igen.")


def tränaPåAtomvikt():
    '''Skriver ut slumpatAtomnamn till slumpad atom och frågar användaren vilken atomvikt atomen i fråga har. Tre alternativ presenteras varav en är slumpadAtomvikt
       och de två andra slumpas (atombeteckningen slumpadAtomnbeteckning får ej förekomma). Ordningen i vilken dessa alternativ skrivs ut randomiseras.'''
    pass
       

#Huvudprogram
   
def huvudprogram():
    '''Algoritm:
    1. Skriver ut en välkommen-hälsning och introducerar programmets funktion
    2. Öppnar, läser in från en fil innehållande alla atombeteckningar samt tillhörande nummer och låter dessa vara attribut i atom-objekt. Objekten läggs till i listan 'atomer'
    3. Definierar ett objekt av klassen periodisktSystem kallat periodiskaSystemet
    4. Anropar funktionen som skriver ut huvudmenyn
    5. Användaren kan välja mellan att 1) Visa det periodiska systemet 2) Träna på atomnummer 3) Träna på atombeteckningar 4) Avsluta
    6. Så länge inte användaren väljer att avsluta programmet exekveras den valda funktionen, sedan kommer användaren tillbaka till huvudmenyn
    7. Programmet avslutas'''
    print("Välkommen till programmet som hjälper dig att bemästra det periodiska systemet!")
    atomer = läsInFrånFil()
    periodiskaSystemet = periodisktSystem(atomer)
    while True:
        menyval = skrivUtHuvudmeny()
        if menyval == "1":
            periodiskaSystemet.visaAtomer()
            continue
        elif menyval == "4":
            print("Tack för idag! Programmet avslutas.")
            break  
        slumpadAtom = periodiskaSystemet.slumpaAtom()
        if menyval == "2":
            väljaÖvningsmetod('atomnummer', str(slumpadAtom.nummer), slumpadAtom.namn)
        elif menyval == "3":
            väljaÖvningsmetod('atombeteckning', slumpadAtom.beteckning, slumpadAtom.namn)    
        else:
            print("Felaktig inmatning. Vänligen ange 1,2,3 eller 4 för något av alternativen ovan.")
huvudprogram()

# Titel: Periodiska Systemet
# Uppgiftsnummer: 178
# Författare: Sara Wahlqvist
# Datum: 2024-12-08
# Detta program kan änvändas för att träna på det periodiska systemet
# Användaren kan välja mellan att visa en lista av alla atomer i det periodiska systemet, alternativt att förhöra sig själv på atomnummer eller atombeteckningar
# Programmet inhämtar atombeteckningar, atomnummer, atommassor och atomnamn från filen 'www.csc.kth.se/~lk/P/avikt.txt' som tillhandahålls av kurslärare
# Datastrukturer: atom-objekten lagras i en lista vid namn 'atomer'
# Klasser: 1) klass som beskriver en atom. Attribut: atombeteckning - förkortning av atomnamn av datatypen sträng, atomvikt - av datatypen flytttal, atomnamn - av datatypen sträng,
#atomnummer - av datatypen heltal
#2) klass som beskriver ett periodiskt system. Attribut: atomlista (lista)

import random
'''Modul som gör det möjligt att randomisera, t.ex. slumpa ett objekt ur en lista. Krävs för funktionen slumpaAtom()'''

#import keyboard
'''Modul som gör det möjligt för användaren att ge input genom att trycka på tangenter. '''
#Denna modul hade jag tänkt att implementera inför nästa inlämning. Jag vill att användaren ska kunna fortsätta generera frågor av önskad sort genom att trycka på enter
#och kunna välja när den vill återgå till huvudmenyn, då via esc.

class Atom:
    '''Klass som beskriver en atom'''
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

    def __lt__(self, other):
        '''Anropas när en lista av objekt av klassen atom sorteras, t.ex. atomer.sorted(). Sorterar atomerna i stigande ordning med avseende på atomnummer.
           Inparameter: self, other
           Returvärde: -'''
        return self.nummer < other.nummer

class periodisktSystem:
    '''Klass som beskriver ett periodiskt system'''
#Metoder
    def __init__(self, atomlista):
        '''Skapar ett periodiskt system
        Inparametrar: self, atomlista (lista)'''
        self.atomlista = atomlista

    def visa(self):
        '''Skriver ut den representerande strängen för varje atom i attributet "atomlista"
           Inparameter: self'''
        self.atomlista.sort()
        for atom in self.atomlista:
            print(atom)

    def slumpaAtom(self):
        '''Slumpar fram en atom ur atomlista
           Inparameter: self
           Returvärde: slumpad atom (objekt)'''
        return random.choice(self.atomlista)    
       
#Funktioner
def läsInFrånFil():
    '''Öppnar tillfälligt importfilen och skapar ett nytt objekt för varje rad i filen. Objektens attribut definieras av radens samtliga textstycken separerade med " ".
       Atomvikten och atomnumret konverteras från sträng till flyt- och heltal.
       Samtliga objekt läggs till i en lista vid namn 'atomer'
       Inparameter: -
       Returvärde: 'atomer' (lista) '''
    with open("avikt.txt","r", encoding="utf-8") as atomfil:
        atomer = []
        for rad in atomfil:
            atombeteckning, atomnummer, atomnamn, atomvikt = rad.strip().split(" ")
            atom = Atom(atombeteckning.strip(), int(atomnummer.strip()), atomnamn.strip(), float(atomvikt.strip()))
            atomer.append(atom)
        return atomer

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
   

def svaraPåFråga(fråga, frågeparameter, svar):
    '''Funktionen ger användaren max tre försök att besvara övningsuppgiften. Efter tre felaktiga försök, alternativt om funktionen ärInmatningRätt returnerar True kommer användaren
       tillbaka till huvudmenyn. 
       Inparametrar: fråga (str), frågeparameter (jobbar på bättre namn)(str), svar(str/int/float)'''
    while True:
        for försök in range(3):
            inmatning = input(f'{frågeparameter} {fråga}')
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
    '''Skriver ut slumpadAtombeteckning och frågar användaren vilken atomvikt atomen i fråga har. Tre alternativ presenteras varav en är slumpadAtomvikt
       och de två andra slumpas (atombeteckningen slumpadAtomnbeteckning får ej förekomma). Ordningen i vilken dessa alternativ skrivs ut randomiseras.
       Felhantering: try-except sats
       Inparameter: ej definierat än'''
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
            periodiskaSystemet.visa()
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

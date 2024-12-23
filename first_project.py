import string
"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Roman Nieslanik
email: r.nieslnanik@gmail.com
"""
##definice
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]
uziv_jmeno = None
vybrane_cislo = None
heslo = None

první_velike_pismeno = 0
veliká_písmena = 0
malá_písmena = 0
cisla = 0
součet_čísel = 0
vybrane_cislo_moznosti = ("1", "2", "3")

# seznam uzivatelů
uzivatele = {
    "bob": "123",
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"}

print("Vítejte v aplikaci na analýzu textu.")
uziv_jmeno = input("Vložte vaše uživatelské jméno:\n")
uziv_jmeno = uziv_jmeno.casefold()      #převedení vstupu na malé písmena
heslo = input("Vložte vaše heslo:\n")

#zobrazení zadaného uživatelského jména a hesla
print("-" * 30)
print("uživatelské jméno:", uziv_jmeno)
print("heslo:", heslo)
print("-" * 30)


#ověření uživatele
if uziv_jmeno in uzivatele and heslo == uzivatele[uziv_jmeno]:
    print("Vítej", uziv_jmeno, " v aplikaci Analýzator textu.\nMáme na výběr tři texty k analýze.")
    vybrane_cislo = input("Pro výběr textu zadej číslo od 1 do 3 ")
    if not vybrane_cislo.isdigit(): # ověření vstupního čísla
        print("Nevložil jste požadované číslo\nKonec programu.")
        exit()
    
    elif vybrane_cislo not in vybrane_cislo_moznosti: #ověření rozsahu
        print("Zadal jste číslo mimo rozsah,\nKonec programu.")
        exit()
    
    else:
        vybrane_cislo = int(vybrane_cislo)    
        print("-" * 30)
        jednotliva_slova = (TEXTS [vybrane_cislo -1].split() )
        jednotliva_slova = [slovo.strip(string.punctuation) for slovo in jednotliva_slova]
        pocet_slov = len(jednotliva_slova)            
        print( "Vybraný text obsahuje", pocet_slov, " slov." )
                
        for slovo in jednotliva_slova:
                if slovo.istitle():
                    první_velike_pismeno += 1
                if slovo.isupper()and slovo.isalpha():
                    veliká_písmena += 1
                if slovo.islower():
                    malá_písmena += 1
                if slovo.isdigit():
                    cisla += 1
                    součet_čísel += int(slovo)
            
        print("Počet slov začínajících velkým písmenem:", první_velike_pismeno)
        print("Počet slov psaných velkými písmeny:", veliká_písmena)
        print("Počet slov psaných malými písmeny:", malá_písmena)
        print("Počet čísel:", cisla)
        print("Součet čísel:", součet_čísel)
        print("-" * 30)
        print("LEN|  ČETNOST  VÝSKYTU  |NR")
        delky_slov = {}
        for slovo in jednotliva_slova:  #úprava statistiky, přidání f stringu
            vypocet = len(slovo)
            if vypocet in delky_slov:
                delky_slov[vypocet] += 1
            else:
                delky_slov[vypocet]  = 1 
                
        for delka, cetnost in sorted(delky_slov.items()):
            print(f"{delka:2} | {'*' * cetnost:<17} | {cetnost}")
            
            
    
    
          
# ukončení programu při zadání špatného jména nebo hesla
else:
    print("uživatelské jméno: ", uziv_jmeno)
    print("heslo: ", heslo)
    print("Neregistrovaný uživatel nebo špatné heslo")
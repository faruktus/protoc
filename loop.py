import json 

dicti_liste = {"1": "Burger", "2": "Schnitzel", "3": "Schweinsbraten", "4": "Sauerkraut"} 

dicti={}
listi=[]
auswahl=""
uebergabe=""

while True:
    uebergabe = auswahl

    print(dicti_liste)
    auswahl = input("Auswahl: ")
    if auswahl != "aus" and (uebergabe == "" or auswahl == uebergabe):
        texti = input("Text: ")
        listi.append(texti)
    elif auswahl != "aus" and auswahl != uebergabe:
        dicti[uebergabe] = listi
        listi=[]
        continue
    else:
        dicti[uebergabe] = listi
        break
    
print(dicti)
        
with open ("data.json", "w") as f:
    json.dump(dicti, f)



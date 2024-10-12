import json 

dicti_liste = {"1": "Burger", "2": "Schnitzel", "3": "Schweinsbraten", "4": "Sauerkraut"} 

dicti={}
listi=[]
auswahl=""
texti=""
uebergabe=""

status=1    
stat=True
while stat == True:
    uebergabe = auswahl
    
    print(dicti_liste)
    auswahl = input("Auswahl: ")
    if auswahl == "aus" or texti == "aus":
        try:
            print("try")
            listi=dicti[uebergabe]
            listi.append(texti)
            dicti[uebergabe]=listi
        except:
            print("except")
            listi=[texti]
            dicti[uebergabe]=listi
        break
            
    while texti != "change":
        texti = input("Text: ")
        if texti == "change":
            texti = "reload"
            break
        elif texti == "aus":
            stat == False
            break
        else:
            try:
                print("try inside")
                listi=dicti[uebergabe]
                listi.append(texti)
                dicti[uebergabe]=listi
            except:
                print("except inside")
                listi=[texti]
                dicti[uebergabe]=listi
            continue 
        
"""
    if uebergabe == "" or auswahl == uebergabe:
        try:
            print(uebergabe)
            listi=dicti[uebergabe]
            listi.append(texti)
            dicti[uebergabe]=listi
        except:
            listi.append(texti)
        print("Erste if")

    elif auswahl != uebergabe:
        dicti[uebergabe]=listi
        listi=[]
        listi.append(texti)
        print("Zweite if")
"""
print(dicti)

            
    
with open ("data.json", "w") as f:
    json.dump(dicti, f)



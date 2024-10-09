import math

def szog():

    vSzam = float(input("Kérem adjon megegy számot!"))
    if (vSzam >= 0) and (vSzam <= 360):
        if vSzam == 0:
            print(str(vSzam) + " -> nullszög")
        elif (vSzam > 0) and (vSzam < 180):
            print(str(vSzam) + " -> hegyesszög")
        elif vSzam == 90:
            print(str(vSzam) + " -> derékszög")
        elif (vSzam > 90) and (vSzam < 180):
            print(str(vSzam) + " -> tompaszög")
        elif vSzam == 180:
            print(str(vSzam) + " -> egyenesszög")
        elif (vSzam > 180) and (vSzam < 360):
            print(str(vSzam) + " -> homurú szög")
        elif vSzam == 360:
            print(str(vSzam) + " -> teljesszög")
    else:
        print("HIBA: Nem megfelelő szám")

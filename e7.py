import math
def negyzetgyok():
    szam = float(input("Adjon meg egy számot!"))
    if szam >= 0:
        gyok = math.sqrt(szam)
        print(gyok)
    else:
        print("HIBA: negatív szám gyökét akarja számolni!")

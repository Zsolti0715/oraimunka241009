def kocka():
    el = int(input("Kérem adjon meg egy él értékét!"))
    if el<=0:
        print("Hiba:  a kocka élének a hossza nem pozitív!")
    else:
        felszin = 6* el**2
        terfogat = pow (el,3)
        print("A kocka felszíne: "+str(felszin)+", térfogata: "+str(terfogat)+".")


from beolvas import  *
from random import *

def egyAlap():
    szam1 = beolvasEgesz()
    if szam1%2 == 1:
        print("Páratlan.")
    else:
        print("Páros.")

def egyAlapA():
    szam1 =randint(-10,10)
    print(szam1)
    if szam1%2 == 1:
        print("Páratlan.")
    else:
        print("Páros.")

def egyAlapA():
        szam1 = randint(-10, 10)
        while not szam1%2 == 0:
            szam1 = randint(-10,10)
            print(szam1)
        print(szam1**2)
def egyalapB():
        szam1= randint(-10,10)
        while not(szam1%2==0):
            szam1 = randint(-10,10)
        print(szam1**2)


def egyalapC():
    szam1 = generalParosEgesz()
    print(szam1 ** 2)

def kettoAlap():
    szam1 = beolvasEgesz()
    if (szam1 >=1) and (szam1<=12):
        if szam1 == 1:
            print("Január")
        elif szam1 ==2:
            print("Február")
        elif szam1 ==3:
            print("Március")
        elif szam1 ==4:
            print("Április")
        elif szam1 ==5:
            print("Május")
        elif szam1 ==6:
            print("Június")
        elif szam1 ==7:
            print("Július")
        elif szam1 ==8:
            print("Augusztus")
        elif szam1 ==9:
            print("Szeptember")
        elif szam1 ==10:
            print("Október")
        elif szam1 ==11:
            print("November")
        else:
            print("December")
    else:
        Print("Hiba: Nem megfelelő szám!")
def kettoAlapA():
    #szam1 = randint(1,12) csak jó
    szam1 = randint(-5, 15) #kevés rossz
    #szam1 = randint(-100,100) sok rossz
    print("Hónap sorszáma:"+str(szam1))
    if (szam1 >=1) and (szam1<=12):
        if szam1 == 1:
            print("Január")
        elif szam1 ==2:
            print("Február")
        elif szam1 ==3:
            print("Március")
        elif szam1 ==4:
            print("Április")
        elif szam1 ==5:
            print("Május")
        elif szam1 ==6:
            print("Június")
        elif szam1 ==7:
            print("Július")
        elif szam1 ==8:
            print("Augusztus")
        elif szam1 ==9:
            print("Szeptember")
        elif szam1 ==10:
            print("Október")
        elif szam1 ==11:
            print("November")
        else:
            print("December")
    else:
        print("Hiba: Nem megfelelő szám!")


def kettoAlapB():
    # szam1 = randint(1,12) csak jó
    szam1 = randint(-5, 15)  # kevés rossz
    # szam1 = randint(-100,100) sok rossz
    print("Hónap sorszáma:" + str(szam1))
    if (szam1 >= 1) and (szam1 <= 12):
        if szam1 == 1:
            print("Január")
        elif szam1 == 2:
            print("Február")
        elif szam1 == 3:
            print("Március")
        elif szam1 == 4:
            print("Április")
        elif szam1 == 5:
            print("Május")
        elif szam1 == 6:
            print("Június")
        elif szam1 == 7:
            print("Július")
        elif szam1 == 8:
            print("Augusztus")
        elif szam1 == 9:
            print("Szeptember")
        elif szam1 == 10:
            print("Október")
        elif szam1 == 11:
            print("November")
        else:
            print("December")
    else:
        print("Hiba: Nem megfelelő szám!")

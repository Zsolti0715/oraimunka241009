import math


def harom():
    pass
    for i in range(21):
        print(i,)
def negy():
    pass
    for i in range(20,58,2):
        print(i,)

def ot():
    pass
    for i in range(77,-80,-4):
        print(i, end=-77)
def beolvas():
    szam = int(input("Kérem adjon meg egy egész számot! "))
    return szam
def beolvas2():
    szam = float(input("Kérem adjon meg egy számot! "))
    return szam

def hat():
    szam1 = beolvas()
    szam2 = beolvas()
# melyik a nagyobb?
    if szam2 < szam1:
        #csere
        atmenet = szam1
        szam1 = szam2
        szam2 = atmenet
    for i in range(szam1, szam2+1,-1):
        print(i, end=" ")
    #6.	Kérj be 2 számot, majd írasd ki a számokat a legkisebbtől a legnagyobbig! (a legnagyobbat is! Ha az első szám nagyobb, abban az esetben is a legkisebbtől a legnagyobbig írasd ki!)

def het():
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat>0:
        for i in range(0, szorzat+1,1):
            print(i, end=" ")
    else:
        for i in range(0,szorzat-1,-1):
            print(i,end=" ")


   #for i in range():
        #print(i,)

def nyolc():
    #8.	Írd meg a fenti feladatot while és for ciklussal is!
    szam1 = beolvas()
    szam2 = beolvas()
    szorzat = szam1 * szam2

    if szorzat < 0:
        i=0
        while i < szorzat - 1:
            print(i, end=" ")
            i-=1
    else:
        i=0
        while i < szorzat+1:
            print(i, end=" ")
            i += 1

def kilenc():
    #for i in range (1,8):
        #print (i,end=",")
    for szam in range (1,8,1):
        print(szam, end=",")
def kilenca():
   #első megoldás
  """  for szam in range (0,7,1):
        print(szam, end=",")
    print(7)
#2. megoldás
         print(0)
        for szam in range(1,8,1):
            print(","+str(szam),end="")"""

def tizenegyedik():
    x = beolvas2()
    y = beolvas2()

    eredmeny = 3*x+y**2
    eredmeny1 = 3 * x + math.pow(y,2)
    eredmeny2 = 3 * x + pow(y,2)
    eredmeny3 = 3 * x + (y*y)
    print("3*"+str(x)+"+"+str(y)+"^2="+str(eredmeny))

def tizenketto():
    x = beolvas2()
    y = beolvas2()
    #print (math.floor(x))
    #print (math.ceil (y))
    db = 0
    for szam in range (math.ceil(x) ,round(y)+1,1):
        #print(szam, end=" ")
        if szam%2 == 0:
            #páros
            db += 1
    print("A páros számok száma: "+str(db)+"db.")

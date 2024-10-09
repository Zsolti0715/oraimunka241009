def egeszbeolvas():
    szam =float(input("Kérem adjon meg egy egész számot"))
    return szam

def teglalap():
    oldal1 = egeszbeolvas()
    oldal2 = egeszbeolvas()

    if (oldal1>0) and (oldal2>0):
        kerulet = round(2*(oldal1+oldal2),2)
        terulet = round(oldal1 * oldal2,2)
        print("A téglalap kerülete: "+str(kerulet)+", terület: "+str(kerulet))
    else:
        print("Hiba: a téglalap oldalai nem pozitívak! ")

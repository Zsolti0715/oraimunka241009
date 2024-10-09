import math
#from math import pow
def kor():
    r = input(" Kérem adjon megy egy kör sugár értékét! ")
    if r > 0:
        terület = r**2 * math.pi
        terület2 = r*r * math.pi
        terület3 = math.pow(r,  2) * math.pi
        terulet4 = pow(r, 2)* math.pi
        kerület = 2 * r * math.pi

        print(" A kör területe: "+str(terulet+" a kör kerülete: "+str(kerulet)+"."))
    else:
        print("HIBA: a kör sugara nem pozitív!")

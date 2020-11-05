import math
import random

x=0
y=0

def sprawdzenie_wyniku(wynik):
    if wynik == x*y:
        return True
    else:
        return False


def wylosuj_mnoznik():
    a = random.randint(1,10)
    return a


kontynuuj="t"
while kontynuuj == "t":


    x = wylosuj_mnoznik()
    y = wylosuj_mnoznik()

    print('podaj wynik mnozenia:',x,'razy',y)

    wynik = int(input())

    print (sprawdzenie_wyniku(wynik))

    kontynuuj = input('chcesz kontynuować t/n?')


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
    a = random.randint(2,9)
    return a



kontynuuj="t"

# główna pęta programu
while kontynuuj == "t":
    punkty = 0
    while punkty<10:

        x = wylosuj_mnoznik()
        y = wylosuj_mnoznik()

        print('podaj wynik mnozenia:',x,'razy',y)

        wynik = int(input())
        if sprawdzenie_wyniku(wynik)==True:
            print ('gratulacje, poprawna odpowiedź, zdobywasz punkt')
            punkty +=1

        else:
            while sprawdzenie_wyniku(wynik)==False:
                print('niestety to zła odpowiedż spróbuj jeszcze raz')
                wynik = int(input())
            else:
                print ('gratulacje, poprawna odpowiedź, zdobywasz punkt')
                punkty += 1
        print('twoj aktualny wynik = ', punkty, 'jeszcze', 10 - punkty, 'poprawnych odpowiedzi i wygrasz')
       # kontynuuj = input('chcesz kontynuować t/n?')

    print ('brawo  ! zdobyłeś 10 punktów !')
    print ('jestes MISTRZEM TABLCZKI MNOZENIA do 100 !')
    print(' + + + +  ')

    print('|\/\/\/\|')
    print('|       |')
    print('---------')

    kontynuuj = input('chcesz kontynuować t/n?')
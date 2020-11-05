from sklep.magazyn import produkty
from sklep.tworzenie_zamowienia import stwoz_zamowienie
from sklep.tworzenie_zamowienia import zamowienia
from sklep.tworzenie_zamowienia import zaktualizuj_magazyn


def uruchom_sklep():
    print(f'witaj w sklepie z masłem i chlebem')
    print(f'1 chleb kosztuje',produkty['chleb']["price"],'PLN')
    print(f'kostka masła kosztuje',produkty['masło']["price"],'PLN')

    sklep_kontynuuj='t'
    while sklep_kontynuuj=='t':
        produkt = input("podaj produkt (chleb lub masło)")
        ilosc = int(input("podaj ilość do zamówienia"))

        stwoz_zamowienie(produkt, ilosc)
        #print(stwoz_zamowienie(produkt, ilosc))
        zaktualizuj_magazyn(produkt, ilosc)
        print('twoje zamówienie zawiera:',zamowienia.pop())
        print("aktualnie w magazynie jest:",produkty)
        sklep_kontynuuj=input('chcesz złożyć kolejne zamówienie? t/n')

if __name__=='__main__':
    uruchom_sklep()
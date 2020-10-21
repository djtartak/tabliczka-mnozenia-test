from sklep.magazyn import produkty
from sklep.tworzenie_zamowienia import stwoz_zamowienie
from sklep.tworzenie_zamowienia import zamowienia
from sklep.tworzenie_zamowienia import zaktualizuj_magazyn

produkt = input("podaj produkt (chleb lub masło)")
ilosc = int(input("podaj ilość do zamówienia"))


print(stwoz_zamowienie(produkt, ilosc))
zaktualizuj_magazyn(produkt, ilosc)
print(zamowienia)
print("aktualnie w magazynie jest:",produkty)
from sklep.tworzenie_zamowienia import stwoz_zamowienie
from sklep.tworzenie_zamowienia import zamowienia

produkt = input("podaj produkt (chleb lub masło)")
ilosc = int(input("podaj ilość do zamówienia"))


print(stwoz_zamowienie(produkt, ilosc))
print(zamowienia)
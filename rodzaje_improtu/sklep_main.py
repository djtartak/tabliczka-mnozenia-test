from sklep.zamowienia import stwoz_zamowienie
from sklep.zamowienia import zamowienia

produkt = input("podaj produkt (chleb lub masło)")
ilosc = int(input("podaj ilość do zamówienia"))


print(stwoz_zamowienie(produkt, ilosc))
print(zamowienia)
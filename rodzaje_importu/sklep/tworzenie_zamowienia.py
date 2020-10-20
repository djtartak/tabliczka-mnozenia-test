from sklep.magazyn import produkty

zamowienia = []

produkt = "chleb"
ilosc = 10


def stwoz_zamowienie(produkt, ilosc):
    cena = produkty[produkt]["price"]
    cena_razem = cena * ilosc

    nowe_zamowienie = {
        "produkt": produkt,
        "cena_razem": cena_razem,
        "ilosc": ilosc,
                   }
    zamowienia.append(nowe_zamowienie)
    return nowe_zamowienie


#stwoz_zamowienie(produkt, ilosc)
#print(zamowienia)

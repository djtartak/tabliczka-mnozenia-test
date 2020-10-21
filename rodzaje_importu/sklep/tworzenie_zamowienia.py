from sklep.magazyn import produkty

zamowienia = []

produkt = "chleb"
ilosc = 10


def stwoz_zamowienie(produkt, ilosc):
    cena = produkty[produkt]["price"]
    cena_razem = cena * ilosc

    if ilosc > produkty[produkt]["quantity"]:
        print('nie mamy aż tyle produktu',produkt)


    nowe_zamowienie = {
        "produkt": produkt,
        "cena_razem": cena_razem,
        "ilosc": ilosc,
                   }
    zamowienia.append(nowe_zamowienie)
    return nowe_zamowienie

def zaktualizuj_magazyn(produkt,ilosc):
    if ilosc < produkty[produkt]["quantity"]:
        produkty[produkt]["quantity"] -= ilosc


#stwoz_zamowienie(produkt, ilosc)
#print(zamowienia)

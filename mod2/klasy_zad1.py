# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
#
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
#
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów,
# a wartościami instancje klasy produkt.

class Produkt:
    pass


class Zamowienie:
    pass


class Jablko:
    pass


class Ziemniak:
    pass


ziemniak_mlody = Ziemniak()
ziemniak_stary = Ziemniak()

jablko_zielone = Jablko()
jablko_czerwone = Jablko()

print('ziemniak_mlody to obiekt typu',type(ziemniak_mlody))
print('ziemniak_stary to obiekt typu',type(ziemniak_stary))
print('jablko_czerowne to obiekt typu',type(jablko_czerwone))

zamowienie_1 = Zamowienie()
zamowienie_2 = Zamowienie()
zamowienie_3 = Zamowienie()
zamowienie_4 = Zamowienie()
zamowienie_5 = Zamowienie()


lista_zamowien =[zamowienie_1,zamowienie_2,zamowienie_3,zamowienie_4,zamowienie_5]

produkty = {
    'ziemniak': Produkt(),
    'jablko': Produkt(),
    'maslo': Produkt(),
    'chleb': Produkt(),
}
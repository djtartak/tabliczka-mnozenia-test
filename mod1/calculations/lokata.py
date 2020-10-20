
def obliczlokate(wart_pocz, procent, liczba_lat):

    wart = wart_pocz * (1 + procent/100) ** liczba_lat

    return wart

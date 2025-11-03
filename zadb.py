def pomnoz_przez_dwa(lista):
    nowa_lista = []
    for liczba in lista:
        nowa_lista.append(liczba * 2)
    return nowa_lista

liczby = [1, 2, 3, 4, 5]
wynik = pomnoz_przez_dwa(liczby)
print(wynik)


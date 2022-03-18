import sys


class Magazyn:
    def __init__(self):
        self.stan_konta = 0
        self.magazyn = {}
        self.historia = []

    def saldo(self, wartosc, komentarz):
        if wartosc == 0:
            print('Wpłać ciut więcej ;)')
            return False, 'Wpłać ciut więcej ;)'
        if self.stan_konta + wartosc < 0:
            print('Zla kwota, brak mozliwosci wyplaty')
            return False, 'Zla kwota, brak mozliwosci wyplaty'
        if komentarz == "stop":
            print("Transakcja anulowana")
            return False, "Transakcja anulowana"
        self.stan_konta += wartosc
        historia_saldo = ("saldo", wartosc, komentarz)
        self.historia.append(historia_saldo)
        return True, f"Sukces! Zaksięgowano: {wartosc}"

    def zakup(self, produkt, cena, ilosc):
        if cena <= 0:
            print('Zla cena!')
            return False, 'Zla cena!'
        if cena > self.stan_konta:
            print('Brak srodkow na zakup')
            return False, 'Brak srodkow na zakup'
        if ilosc <= 0 or ilosc * cena > self.stan_konta:
            print('Brak srodkow na zakup')
            return False, 'Brak srodkow na zakup'
        self.stan_konta -= cena * ilosc
        if produkt in self.magazyn:
            self.magazyn[produkt] += ilosc
        else:
            self.magazyn[produkt] = ilosc
        historia_zakup = ("zakup", produkt, cena, ilosc)
        self.historia.append(historia_zakup)
        return True, f"Sukces! Zakupiono: {produkt}"

    def sprzedaz(self, produkt, cena, ilosc):
        if produkt not in self.magazyn:
            print('Brak produktu w magazynie!')
            return False, 'Brak produktu w magazynie!'
        if cena <= 0:
            print('Zla cena!')
            return False, 'Zla cena!'
        if ilosc <= 0:
            print('Zła ilość!')
            return False, 'Zła ilość!'
        if self.magazyn[produkt] < ilosc:
            print('Brak takiej ilosci w magazynie')
            return False, 'Brak takiej ilosci w magazynie'
        self.stan_konta += cena * ilosc
        self.magazyn[produkt] -= ilosc
        historia_sprzedaz = ("sprzedaz", produkt, cena, ilosc)
        self.historia.append(historia_sprzedaz)
        return True, f"Sukces! Sprzedano: {produkt}"

    def przeglad(self, start, end):
        print(self.historia[start:end+1])
        for wiersz in self.historia[start:end+1]:
            for element in wiersz:
                print(element)
        return True, f'Zakres zmieniony! Wyświetlam od: {start} do: {end}'

    def magazyn_show(self):
        for quantity_of_argv in range(len(sys.argv[2:])):
            if sys.argv[quantity_of_argv + 2] not in magazyn:
                magazyn[sys.argv[quantity_of_argv + 2]] = 0
            print(sys.argv[quantity_of_argv + 2], ":", magazyn[sys.argv[quantity_of_argv + 2]])

    def wczytaj(self, path):
        with open(path, "r") as file:
            while True:
                line=file.readline().strip()
                if line == "saldo":
                    wartosc = int(file.readline().strip())
                    komentarz = file.readline().strip()
                    self.saldo(wartosc, komentarz)
                if line == "zakup":
                    produkt = file.readline().strip()
                    cena = int(file.readline().strip())
                    ilosc = int(file.readline().strip())
                    self.zakup(produkt, cena, ilosc)
                if line == "sprzedaz":
                    produkt = file.readline().strip()
                    cena = int(file.readline().strip())
                    ilosc = int(file.readline().strip())
                    self.sprzedaz(produkt, cena, ilosc)
                if line == "stop":
                    break

    def zapisz(self, path):
        with open(path, "w") as file:
            for line in self.historia:
                for element in line:
                    file.write(f"{element}\n")
            file.write("stop")
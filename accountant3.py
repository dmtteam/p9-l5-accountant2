import sys


class Manager:
    def __init__(self):
        self.stan_konta = 0
        self.magazyn = {}
        self.historia = []
        self.actions = {}
# name = ["saldo", "zakup", "sprzedaz", "konto", "magazyn", "przeglad", "stop"]

    def assign(self, name,counter):
        def decorate(cb):
            self.actions[name] = cb, counter
        return decorate

    def execute(self, name,params):
        if name not in self.actions:
            print("Action not defined")
        else:
            cb=self.actions[name][0]
            cb(self,*params)
# self.actions[name](self)

    def wczytaj(self, path):
        with open(path,  "r") as file:
            while True:
                line=file.readline().strip()
                if line == "stop":
                    break
                cb, counter = self.actions[line]
                params = []
                for i in range(counter):
                    params.append(file.readline().strip())
                cb(self, *params)

    def zapisz(self, path):
        with open(path, "w") as file:
            for line in self.historia:
                for element in line:
                    file.write(f"{element}\n")
            file.write("stop")

manager=Manager()

@manager.assign("saldo",2)
def saldo(manager, wartosc, komentarz):
    wartosc=int(wartosc)
    if wartosc == 0:
        print('Wpłać ciut więcej ;)')
        return False
    if manager.stan_konta + wartosc < 0:
        print('Zla kwota, brak mozliwosci wyplaty')
        return False
    if komentarz == "stop":
        print("Transakcja anulowana")
        return False
    manager.stan_konta += wartosc
    historia_saldo = ("saldo", wartosc, komentarz)
    manager.historia.append(historia_saldo)
    return True

@manager.assign("zakup",3)
def zakup(manager, produkt, cena, ilosc):
    cena=int(cena)
    ilosc=int(ilosc)
    if cena <= 0:
        print('Zla cena!')
        return False
    if cena > manager.stan_konta:
        print('Brak srodkow na zakup')
        return False
    if ilosc <= 0 or ilosc * cena > manager.stan_konta:
        print('Brak srodkow na zakup')
        return False
    manager.stan_konta -= cena * ilosc
    if produkt in manager.magazyn:
        manager.magazyn[produkt] += ilosc
    else:
        manager.magazyn[produkt] = ilosc
    historia_zakup = ("zakup", produkt, cena, ilosc)
    manager.historia.append(historia_zakup)
    return True

@manager.assign("sprzedaz",3)
def sprzedaz(manager, produkt, cena, ilosc):
    cena=int(cena)
    ilosc=int(ilosc)
    if produkt not in manager.magazyn:
        print('Brak produktu w magazynie!')
        return False
    if cena <= 0:
        print('Zla cena!')
        return False
    if ilosc <= 0:
        print('Zła ilość!')
        return False
    if manager.magazyn[produkt] < ilosc:
        print('Brak takiej ilosci w magazynie')
        return False
    manager.stan_konta += cena * ilosc
    manager.magazyn[produkt] -= ilosc
    historia_sprzedaz = ("sprzedaz", produkt, cena, ilosc)
    manager.historia.append(historia_sprzedaz)
    return True

@manager.assign("przeglad",2)
def przeglad(manager, start, end):
    start=int(start)
    end=int(end)
# print(manager.historia[start:end+1])
    for wiersz in manager.historia[start:end+1]:
        for element in wiersz:
            print(element)

@manager.assign("magazyn",0)
def magazyn_show(manager, *params):
    for quantity_of_argv in range(len(sys.argv[2:])):
        if sys.argv[quantity_of_argv + 2] not in manager.magazyn:
            manager.magazyn[sys.argv[quantity_of_argv + 2]] = 0
        print(sys.argv[quantity_of_argv + 2], ":", manager.magazyn[sys.argv[quantity_of_argv + 2]])


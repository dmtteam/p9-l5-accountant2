import sys
from accountant3 import manager

#obj = Manager()
manager.wczytaj(sys.argv[1])
manager.execute("saldo",sys.argv[2:])
manager.zapisz(sys.argv[1])
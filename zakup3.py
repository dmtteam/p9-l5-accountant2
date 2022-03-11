import sys
from accountant3 import manager

#obj = Manager()
manager.wczytaj(sys.argv[1])
# manager.zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
manager.execute("zakup",sys.argv[2:])
manager.zapisz(sys.argv[1])

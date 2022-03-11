import sys
from accountant3 import manager

#obj = Manager()
manager.wczytaj(sys.argv[1])
#manager.przeglad(int(sys.argv[2]), int(sys.argv[3]))
manager.execute("przeglad",sys.argv[2:])
import sys
from accountant3 import manager

#obj = Manager()
manager.wczytaj(sys.argv[1])
manager.execute("magazyn",sys.argv[2:])
#manager.magazyn_show()                  # ?
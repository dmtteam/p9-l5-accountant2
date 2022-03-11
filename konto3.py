import sys
from accountant3 import manager

#obj = Manager()
manager.wczytaj(sys.argv[1])
print(manager.stan_konta)
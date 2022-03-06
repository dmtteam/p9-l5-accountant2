import sys
from brain import Magazyn

obj = Magazyn()
obj.wczytaj(sys.argv[1])
print(obj.stan_konta)



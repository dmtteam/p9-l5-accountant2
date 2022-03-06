import sys
from brain import Magazyn

obj = Magazyn()
obj.wczytaj(sys.argv[1])
obj.saldo(int(sys.argv[2]), sys.argv[3])
obj.zapisz(sys.argv[1])







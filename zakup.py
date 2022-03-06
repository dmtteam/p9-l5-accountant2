import sys
from brain import Magazyn

obj = Magazyn()
obj.wczytaj(sys.argv[1])
obj.zakup(sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))
obj.zapisz(sys.argv[1])





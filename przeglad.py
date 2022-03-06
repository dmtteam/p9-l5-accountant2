import sys
from brain import Magazyn

obj = Magazyn()
obj.wczytaj(sys.argv[1])
obj.przeglad(int(sys.argv[2]), int(sys.argv[3]))

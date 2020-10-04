import sys
import os

print (sys.path)

# import pierwszy
# import drugi

sys.path.append(sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'moduly'))))

print (sys.path)

import pierwszy
import drugi

dir(pierwszy)
dir(drugi)


# Zadanie:
#  Zbuduj program skladajacy sie z dwoch katalogow,
#  po dwa moduly w kazdym katalogu.
#  Umozliwic ladowanie wszystkich modulow
#  do modulu glownego poslugujac sie zmienna PYTHONPATH

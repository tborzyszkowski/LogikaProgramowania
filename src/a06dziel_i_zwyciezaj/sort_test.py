import sys
import os

sys.path.append(sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.'))))

from random import random
from datetime import datetime
from insertion_sort import *
from merge_sort import *

N = 5000

values = [int(random() * N * 1000) for y in range(N)]
t1 = datetime.now()
insertion_sort(values)
t2 = datetime.now()
print("insert sort time:   ", (t2 - t1).total_seconds() * 1000)


values = [int(random() * N * 1000) for y in range(N)]
t1 = datetime.now()
merge_sort(values, 0, len(values) - 1)
t2 = datetime.now()
print("merge sort time:   ", (t2 - t1).total_seconds() * 1000)

values_benchmark = [int(random() * N) for y in range(N)]
t1 = datetime.now()
values_sorted = sorted(values_benchmark)
t2 = datetime.now()
print("builin sorted time:   ", (t2 - t1).total_seconds() * 1000)



from multiprocessing import 
from datetime import datetime

def f(x):
    return x*x

with Pool(5) as p:
    print(p.map(f, [1, 2, 3]))


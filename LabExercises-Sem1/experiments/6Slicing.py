import numpy as np
import pandas as pd
import matplotlib as plt

x = [5, 9, 2, 3, 4, 6, 7, 0, 8, 12, 2, 9]

print(x[1])

print(x[1:4])

print([x[i] for i in [1,2,5]])

print([x[i] for i in range(0,5)] + [x[i] for i in range(9,12)])

print([x[i] for i in range(len(x)) if i not in range(10,12)])
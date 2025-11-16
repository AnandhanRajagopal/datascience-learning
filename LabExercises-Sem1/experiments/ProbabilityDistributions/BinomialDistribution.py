from scipy.stats import binom
import matplotlib.pyplot as plt

n = 10
p = 0.6

r_values = list(range(n+1))

dist = [binom.pmf(r,n,p) for r in r_values]

plt.bar(r_values, dist)

_ = plt.title(f'Binomial distribution')

plt.show()
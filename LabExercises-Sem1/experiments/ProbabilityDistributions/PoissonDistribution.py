from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

k_values = np.arange(0,15)

pmf_values = poisson.pmf(k_values, mu=3)

plt.bar(k_values,pmf_values)

_ = plt.title(f'Poisson  distribution')

plt.show()
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt

mean = 0
std_dev = 1

x = np.linspace(-4,4,100)

print(x)
y = norm.pdf(x,mean, std_dev)

plt.plot(x,y)
plt.title("Normal Distribution( Mean = 0, SD = 1)")
plt.xlabel("X Values")
plt.ylabel("Probability Density")
plt.show()
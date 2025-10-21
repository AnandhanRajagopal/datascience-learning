import matplotlib.pyplot as plt
import numpy as np

companyname = ["Google", "Amazon", "Microsoft", "IBM"]
profit = [3000,5000, 6000, 4500]
plt.figure(figsize=(12,6))

plt.subplot(1,2,1)
plt.bar(companyname, profit)
plt.title("Bar Chart")
plt.xlabel("Company Name")
plt.ylabel("Profit Value")

plt.subplot(1,2,2)
plt.boxplot([profit], label=["Companies"])
plt.title("Box Chart")
plt.ylabel("Profit Value")


plt.tight_layout()
plt.show()
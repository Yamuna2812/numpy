import numpy as np

data = np.genfromtxt("data.csv", delimiter=",")

# column-wise stats
print("Mean:", np.mean(data, axis=0))
print("Max:", np.max(data, axis=0))

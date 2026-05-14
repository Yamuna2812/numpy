import numpy as np

data = np.array([
    [1, 2], [1, 4], [1, 0],
    [10, 2], [10, 4], [10, 0]
])

# random centroids
centroids = data[np.random.choice(len(data), 2)]

for _ in range(5):
    # distance
    dist = np.linalg.norm(data[:, None] - centroids, axis=2)
    
    # assign clusters
    labels = np.argmin(dist, axis=1)
    
    # update centroids
    centroids = np.array([data[labels == i].mean(axis=0) for i in range(2)])

print("Centroids:\n", centroids)

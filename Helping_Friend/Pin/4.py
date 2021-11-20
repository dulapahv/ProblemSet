import numpy as np

def get_euclidean_distance(arr1, arr2):
    return np.linalg.norm(arr1 - arr2)

p1 = np.array([float(input) for input in input(f"Enter coordinate of P1: ").split()])
p2 = np.array([float(input) for input in input(f"Enter coordinate of P2: ").split()])
p3 = np.array([float(input) for input in input(f"Enter coordinate of P3: ").split()])

dist = []
dist.append(get_euclidean_distance(p1, p2))
dist.append(get_euclidean_distance(p2, p3))
dist.append(get_euclidean_distance(p3, p1))

print(f"The longest distance = {max(dist):.2f}")
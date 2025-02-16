import numpy as np

conversionRates = [0.15, 0.04, 0.13, 0.11, 0.05]
N = 10000
d = len(conversionRates)

X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

for i in range(N):
    selected = 0
    maxRandom = 0



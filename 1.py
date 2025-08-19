import numpy as np

def generate_logistic_data(theta, n, m):
    X = np.random.randn(n, m)
    X = np.hstack((np.ones((n, 1)), X))
    beta = np.random.randn(m + 1)
    logits = X @ beta
    probs = 1 / (1 + np.exp(-logits))
    Y = np.random.binomial(1, probs)
    flip_mask = np.random.binomial(1, theta, size=n)
    Y = np.abs(Y - flip_mask)
    return X, Y.reshape(-1, 1), beta

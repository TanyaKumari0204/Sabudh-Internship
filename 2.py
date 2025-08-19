import numpy as np

def learn_logistic_parameters(X, Y, k, tau, lmbda):
    n, m = X.shape
    beta = np.random.randn(m)
    prev_cost = float('inf')
    for _ in range(k):
        logits = X @ beta
        probs = 1 / (1 + np.exp(-logits))
        cost = -np.mean(Y * np.log(probs + 1e-15) + (1 - Y) * np.log(1 - probs + 1e-15))
        gradient = X.T @ (probs - Y.reshape(-1)) / n
        beta -= lmbda * gradient
        if abs(prev_cost - cost) < tau:
            break
        prev_cost = cost
    return beta, cost

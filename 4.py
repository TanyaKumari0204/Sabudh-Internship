import numpy as np

def learn_logistic_parameters_regularised(X, Y, k, tau, lmbda, penalty='l2'):
    n, m = X.shape
    beta = np.random.randn(m)
    prev_cost = float('inf')

    for _ in range(k):
        logits = X @ beta
        probs = 1 / (1 + np.exp(-logits))
        base_cost = -np.mean(Y * np.log(probs + 1e-15) + (1 - Y) * np.log(1 - probs + 1e-15))

        if penalty == 'l2':
            reg_term = (lmbda / (2 * n)) * np.sum(beta[1:] ** 2)
            gradient = (X.T @ (probs - Y.reshape(-1)) + lmbda * np.r_[0, beta[1:]]) / n
        elif penalty == 'l1':
            reg_term = (lmbda / n) * np.sum(np.abs(beta[1:]))
            gradient = (X.T @ (probs - Y.reshape(-1)) + lmbda * np.r_[0, np.sign(beta[1:])]) / n
        else:
            reg_term = 0
            gradient = X.T @ (probs - Y.reshape(-1)) / n

        cost = base_cost + reg_term
        beta -= lmbda * gradient

        if abs(prev_cost - cost) < tau:
            break
        prev_cost = cost

    return beta, cost

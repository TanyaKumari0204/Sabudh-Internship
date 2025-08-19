import numpy as np
import matplotlib.pyplot as plt

def generate_logistic_data(theta, n, m):
    X = np.random.randn(n, m)
    X = np.hstack((np.ones((n, 1)), X))
    beta_true = np.random.randn(m + 1)
    logits = X @ beta_true
    probs = 1 / (1 + np.exp(-logits))
    Y = np.random.binomial(1, probs)
    flip_mask = np.random.binomial(1, theta, size=n)
    Y = np.abs(Y - flip_mask)
    return X, Y.reshape(-1, 1), beta_true

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

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def run_experiment():
    m = 5
    k = 1000
    tau = 1e-6
    lmbda = 0.1
    n_values = [50, 100, 500, 1000]
    theta_values = [0.0, 0.1, 0.3, 0.5]

    results = []

    for n in n_values:
        for theta in theta_values:
            X, Y, beta_true = generate_logistic_data(theta, n, m)
            beta_learned, final_cost = learn_logistic_parameters(X, Y, k, tau, lmbda)
            similarity = cosine_similarity(beta_learned, beta_true)
            results.append((n, theta, similarity, final_cost))

    for r in results:
        print(f"n={r[0]}, θ={r[1]:.2f} → Cosine Similarity: {r[2]:.4f}, Final Cost: {r[3]:.4f}")

run_experiment()

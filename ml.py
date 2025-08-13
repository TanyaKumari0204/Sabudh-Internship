import numpy as np

# 1. Function to generate synthetic linear data
def generate_data(sigma, n, m):
    # Create X with shape (n, m+1), first column is 1s
    X = np.random.rand(n, m)
    X = np.hstack((np.ones((n, 1)), X))  # Add bias term xi0 = 1

    # Generate random coefficients β of shape (m+1,)
    beta = np.random.randn(m + 1)

    # Generate noise e from Gaussian distribution
    e = np.random.normal(0, sigma, size=n)

    # Compute Y = Xβ + e
    Y = X @ beta + e

    return X, Y.reshape(-1, 1), beta


# 2. Function to learn β using Gradient Descent
def learn_beta(X, Y, k, tau, lmbda):
    n, m_plus_1 = X.shape
    beta = np.random.randn(m_plus_1)
    prev_cost = float('inf')

    for i in range(k):
        # Prediction
        Y_pred = X @ beta

        # Error
        error = Y_pred - Y.flatten()

        # Cost function (Mean Squared Error)
        cost = (1 / (2 * n)) * np.sum(error ** 2)

        # Check for convergence
        if abs(prev_cost - cost) < tau:
            break
        prev_cost = cost

        # Gradient
        gradient = (1 / n) * (X.T @ error)

        # Update β
        beta -= lmbda * gradient

    return beta, cost


# 3. Investigation report (basic printout)
def investigate(n_values, sigma_values, m=3):
    print("Investigating impact of n and σ on learning β...\n")
    for n in n_values:
        for sigma in sigma_values:
            X, Y, true_beta = generate_data(sigma, n, m)
            learned_beta, final_cost = learn_beta(X, Y, k=1000, tau=1e-6, lmbda=0.01)
            print(f"n = {n}, σ = {sigma}")
            print("True β:", np.round(true_beta, 3))
            print("Learned β:", np.round(learned_beta, 3))
            print("Final Cost:", round(final_cost, 4))
            print("-" * 40)


# Example usage
if __name__ == "__main__":
    # Run investigation with sample values
    investigate(n_values=[50, 100, 500], sigma_values=[0.1, 1, 5])

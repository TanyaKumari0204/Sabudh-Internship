class BaseRegression:
    def __init__(self, learning_rate, max_iter, tolerance):
        self.lr = learning_rate
        self.max_iter = max_iter
        self.tolerance = tolerance
        self.beta = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, Y):
        raise NotImplementedError

    def predict(self, X):
        raise NotImplementedError

class LinearRegression(BaseRegression):
    def fit(self, X, Y):
        # Implement gradient descent for linear regression
        pass

    def predict(self, X):
        return X @ self.beta

class LogisticRegression(BaseRegression):
    def fit(self, X, Y):
        # Implement gradient descent for logistic regression
        pass

    def predict(self, X):
        logits = X @ self.beta
        return self.sigmoid(logits) > 0.5

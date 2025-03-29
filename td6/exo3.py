import numpy as np

class Perceptron:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weights = None
        self.bias = None
        
    def fit(self, X, y):
        """
        Train the perceptron using the training data.
        
        Parameters:
        X: Training examples, shape (n_samples, n_features)
        y: Target values, shape (n_samples,)
        """
        n_samples, n_features = X.shape
        
        # Initialize weights and bias
        self.weights = np.zeros(n_features)
        self.bias = 0
        
        # Convert y to binary if needed (-1 and 1)
        y_ = np.where(y <= 0, -1, 1)
        
        # Training process
        for _ in range(self.n_iterations):
            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = 1 if linear_output > 0 else -1
                
                # Update weights and bias only if prediction is wrong
                if y_predicted != y_[idx]:
                    update = self.learning_rate * y_[idx]
                    self.weights += update * x_i
                    self.bias += update
                    
    def predict(self, X):
        """
        Predict using the trained perceptron.
        
        Parameters:
        X: Samples to predict, shape (n_samples, n_features)
        
        Returns:
        Predictions, shape (n_samples,)
        """
        linear_output = np.dot(X, self.weights) + self.bias
        return np.where(linear_output <= 0, 0, 1)

# Example usage
if __name__ == "__main__":
    # Sample data for XOR (not linearly separable, will not converge)
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([0, 1, 1, 0])
    
    # Create and train the perceptron
    perceptron = Perceptron(learning_rate=0.1, n_iterations=100)
    perceptron.fit(X, y)
    
    # Make predictions
    predictions = perceptron.predict(X)
    print("Predictions:", predictions)
    print("Actual:     ", y)
    print("Accuracy:", np.mean(predictions == y))
    print("Note: The perceptron cannot solve XOR as it's not linearly separable.")
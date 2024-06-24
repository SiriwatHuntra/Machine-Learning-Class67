import numpy as np

def gradientDescent(n_samples, lr, X, y, y_pred):
    # find best weight
    
    d_weigths = (1 / n_samples) * np.dot(X.T, (y_pred - y)) 
    # d_weights = 1 / n * ∑(y_prediction - y_actual) *  X
    d_bias = (1 / n_samples) * np.sum(y_pred - y)           
    # d_bias = 1 / n * ∑(y_prediction - y_actual)
    
    weights_gradient = lr * d_weigths
    bias_gradient = lr * d_bias
    
    return weights_gradient, bias_gradient

def costFunction(n_samples, y_pred, y):     # Mean Sqaure Error (MSE)
    return (1 / (2 * n_samples)) * np.sum((y_pred - y)**2)

class LinearRegression:

    def __init__(self, lr = 0.001, n_iters = 0):
        self.lr = lr
        self.n_iters = n_iters
        self.weights = 0 # wi
        self.bias = 0 # w0
        self.n_samples = 0
        self.weights_history = []
        self.bias_history = []
        
    # Evaluation + Optimization   
    def training(self, X, y):
        # n => sample, m => features
        n_samples, n_features = X.shape     
        self.n_samples = n_samples          # set default number of samples
        self.weights = np.zeros(n_features) 
        # 1st time => weight = 0
        # weight array n => feature member
        
        for _ in range(self.n_iters):
            y_pred = self.prediction(X)
            weights_gradient, bias_gradient = gradientDescent(n_samples, self.lr, X, y, y_pred)
            self.weights -= weights_gradient
            self.bias -= bias_gradient
            self.weights_history.append(self.weights[0])
            self.bias_history.append(self.bias)
    
    def generate_costs_forContour(self, X, y, w_range, b_range):
        W, B = np.meshgrid(w_range, b_range)
        costs_history = np.zeros(W.shape)
        
        for i in range(len(w_range)):
            for j in range(len(b_range)):
                weights = w_range[i]
                bias = b_range[j]
                y_pred = weights * X[:, 0] + bias
                costs_history[j, i] = costFunction(self.n_samples, y_pred, y)
                
        return W, B, costs_history
    
    def get_Weigths_Bias_History(self):
        return self.weights_history, self.bias_history

    # Representation
    def prediction(self, X):
        # y = wx + b, in the form of matrix calculation y = (w * X) + b
        return np.dot(X, self.weights) + self.bias
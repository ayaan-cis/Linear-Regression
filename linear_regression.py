import matplotlib.pyplot as plt
import numpy as np

my_data = np.genfromtxt('example.csv', delimiter=',')
X = my_data[:, 0].reshape(-1, 1)
ones = np.ones([X.shape[0], 1])
X = np.concatenate([ones, X], 1)
y = my_data[:, 1].reshape(-1, 1)

alpha = 0.0001
iterations = 1000
theta = np.array([[1.0, 1.0]])

def computeCost(X, y, theta):
    inner = np.power(((X @ theta.T) - y), 2)
    return np.sum(inner) / (2 * len(X))

def gradientDescent(X, y, theta, alpha, iterations):
    for i in range(iterations):
        theta = theta - (alpha/len(X)) * np.sum((X @ theta.T - y) * X, axis=0)
        cost = computeCost(X, y, theta)
        # if i % 10 == 0: # just look at cost every ten loops for debugging
        #     print(cost)
    return (theta, cost)

# Example graph plotting
plt.scatter(my_data[:, 0].reshape(-1, 1), y)
g, cost = gradientDescent(X, y, theta, alpha, iterations)
axes = plt.gca()
x_value = np.array(axes.get_xlim())
y_value = g[0][0] + g[0][1]* x_value
plt.plot(x_value, y_value, '--')
plt.show()


# Linear Regression

Linear Regression (linear_regression.py):
Data Preparation: It loads data from 'example.csv', assuming the first column as the feature (X) and the second column as the target variable (y).

Model Initialization: Sets a learning rate (alpha), the number of iterations for the gradient descent, and initializes theta (the parameters of the linear model).

Functions:
computeCost: Calculates the cost using mean squared error.
gradientDescent: Performs the gradient descent algorithm to optimize theta.

Plotting: Plots the data points and the linear regression line after training.

Operation: This script performs simple linear regression with a single feature.




Multivariate Linear Regression (multivariate_lr.py):
Data Preparation: Reads data from 'home.txt' into a DataFrame, normalizes the data, and prepares matrices for features (X) and the target variable (y). Assume the first two columns as features and the third column is the target.

Model Initialization: Similar to the first script, it sets a learning rate and iterations, and initializes theta for a multivariate model.

Functions:

computeCost: Similar to the first script, calculates the cost.
gradientDescent: Optimizes theta for a model with multiple features.

Plotting: Plots the cost over iterations to show how the error decreases as the model learns.

Operation: This script is designed for linear regression with multiple features (multivariate linear regression).

Both scripts are examples of linear regression implementations in Python using NumPy and Matplotlib. The first script is for a simpler case with one feature, and the second handles more complex scenarios with multiple features. Each script includes functions for calculating the cost and performing gradient descent, crucial for training linear regression models. ​

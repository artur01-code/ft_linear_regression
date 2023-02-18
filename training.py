import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Define the estimatePrice function
def estimatePrice(theta0, theta1, mileage):
    return theta0 + theta1 * mileage

# Perform gradient descent
def linear_regression(theta0, theta1, data, learningRate):
    n = len(data)

    for i in range(n):
        km = data["km"].iloc[i]
        price = data["price"].iloc[i]

        # Compute the temporary values for theta0 and theta1 using np.float128
        tmpTheta0 = learningRate * (1 / n) * np.sum(estimatePrice(theta0, theta1, km) - price, dtype=np.float128)
        tmpTheta1 = learningRate * (1 / n) * np.sum((estimatePrice(theta0, theta1, km) - price) * km, dtype=np.float128)

        # Update theta0 and theta1 simultaneously
        theta0 -= tmpTheta0
        theta1 -= tmpTheta1
    return theta0, theta1


if __name__ == "__main__":


    # Read the dataset file
    data = pd.read_csv('data/data.csv')
    plt.scatter(data.km, data.price)


    # Initialize the learning rate and number of iterations
    learningRate = 0.1
    numIterations = 2000

    # Initialize theta0 and theta1 to zero
    theta0 = 0
    theta1 = 0

    # normalize data
    km_max = data["km"].max()
    price_max = data["price"].max()
    data["km"] = data["km"] / km_max
    data["price"] = data["price"] / price_max

    for i in range(numIterations):
        theta0, theta1 = linear_regression(theta0, theta1, data, learningRate)

    # Unnormalize the resulting theta0 and theta1 values
    theta0 *= price_max
    theta1 *= price_max / km_max

    # Save the resulting theta0 and theta1 values to a file
    np.savetxt('theta_values.txt', [theta0, theta1], delimiter=',')

    # Plot the resulting regression line
    plt.scatter(data.km, data.price)
    plt.plot(list(range(250000, 9000)), [theta0 * x + theta1 for x in range (250000, 9000)])
    plt.show

    # Print the resulting theta0 and theta1 values
    print(f"theta0: {theta0}, theta1: {theta1}")



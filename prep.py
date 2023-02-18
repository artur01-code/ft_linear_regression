import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('data/data.csv')

# print(data)
# plt.scatter(data.km, data.price)
# plt.show()


# calcualtes the loss manually
def loss_function(m, b, points):
    total_error: 0
    for i in range(len(points)):
        x = points.iloc[i].km
        y = points.iloc[i].price
        total_error += (y - (m * x + b)) ** 2 
    total_error / float(len(points))

def predict(theta0, theta1, mileage):
    return (theta0 + (theta1 * mileage))

def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].km
        y = points.iloc[i].price

        pred = predict(m_now, b_now, x)

        # m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        # b_gradient += -(2/n) * (y - (m_now * x + b_now))
        m_gradient += L * (1/n) * np.sum(pred - y)
        b_gradient += L * (1/n) * np.sum((pred - y) * x)

    m_now -= m_gradient
    b_now -= b_gradient

    # m = m_now - m_gradient * L
    # b = b_now - b_gradient * L
    return m_now, b_now

m = 0
b = 0
L = 0.1
epochs = 2000

for i in range(epochs):
    m, b = gradient_descent(m, b, data, L)

print(m, b)
plt.scatter(data.km, data.price)
plt.plot(list(range(250000, 9000)), [m * x + b for x in range (250000, 9000)])
plt.show


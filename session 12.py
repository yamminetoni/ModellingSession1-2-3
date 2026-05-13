import numpy as np
import matplotlib.pyplot as plt

# Generate data
# np.random.seed(0)
x = np.linspace(0, 10, 101)
y = 3 * x + 6 + np.random.normal(0, 5, 101)
y2 = 3 * x + 3 + np.random.normal(5 , 1, 101)

# y = 3 * x + 3


# Plot the data points
plt.figure(figsize=(20,10))
plt.scatter(x, y, label='y')
plt.scatter(x, y2, label='y2')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Synthetic Data')
plt.legend()
plt.show()

# Solving for m and b using the normal equations
A = np.vstack([x, np.ones(len(x))]).T # The design matrix
print(A)
m, b = np.linalg.lstsq(A, y, rcond=None)[0]

# Print the values of m and b
print(f"m = {m:.4f}, b = {b:.4f}")

# Plot the best-fitting line
plt.figure(figsize=(20,10))
y_pred = m * x + b
plt.scatter(x, y, label='Data points')
plt.plot(x, y_pred, color='red', label='Best-fitting line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least Squares')
plt.legend()
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample data (square_meter, price)
data = np.array([
    [50, 40000],
    [100, 100000],
    [120, 170000],
    [150, 160000],
    [180, 200000],
    [200, 240000],
    [220, 260000],
    [250, 180000],
    [500, 600000]
])

# Convert the data to a DataFrame
df = pd.DataFrame(data, columns=['Square Meters', 'Price'])

# Calculate the mean of the independent and dependent variables
X_mean = df['Square Meters'].mean()
y_mean = df['Price'].mean()

# Calculate the coefficients
numerator = np.sum((df['Square Meters'] - X_mean) * (df['Price'] - y_mean))
denominator = np.sum((df['Square Meters'] - X_mean)**2)
m = numerator / denominator
b = y_mean - m * X_mean # y = b + mx -> b = y - mx

# Print the coefficients
print(f"Intercept: {b}, Coefficient: {m}")

# Plot the data points and the fitted line
plt.figure(figsize=(20,10))
plt.scatter(df['Square Meters'], df['Price'], color='blue')
plt.plot(df['Square Meters'], m * df['Square Meters'] + b, color='red')
plt.xlabel('Square Meters')
plt.ylabel('Price')
plt.title('Simple Linear Regression: House Price vs. Size')
plt.show()
house_300 = 300*m + b
print(house_300)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Convert to DataFrame for ease of manipulation
df = pd.DataFrame(data, columns=['Square Meters', 'Price'])

# Using the matrix method
A = np.vstack([df['Square Meters'], np.ones(len(df))]).T
m, b = np.linalg.lstsq(A, df['Price'], rcond=None)[0]

# Print the coefficients
print(f"Intercept: {b}, Coefficient: {m}")

# Plot the data points and the fitted line
plt.figure(figsize=(20, 10))
plt.scatter(df['Square Meters'], df['Price'], color='blue')
plt.plot(df['Square Meters'], m * df['Square Meters'] + b, color='red')
plt.xlabel('Square Meters')
plt.ylabel('Price')
plt.title('Simple Linear Regression: House Price vs. Size')
plt.show()

# Predicting the house price for 300 square meters
house_300 = 300 * m + b
print(house_300)

import numpy as np
import matplotlib.pyplot as plt

def gradient_descent(x, y, learning_rate=0.01, epochs=10):
    m, b = 0.0, 0.0
    n = len(x)

    for _ in range(epochs):
        y_pred = m * x + b
        dm = (-2/n) * np.sum(x * (y - y_pred))
        db = (-2/n) * np.sum(y - y_pred)
        m -= learning_rate * dm
        b -= learning_rate * db

    return m, b

# Generate synthetic data
# np.random.seed(0)
x = np.linspace(0, 10, 100)
y = 3 * x + 2 + np.random.normal(0, 3, 100)

# Linear least squares solution
A = np.vstack([x, np.ones(len(x))]).T
m_ls, b_ls = np.linalg.lstsq(A, y, rcond=None)[0]

# Gradient descent solution
m_gd, b_gd = gradient_descent(x, y, 0.01, 20) #try different values

# Plot the data points, least squares line, and gradient descent line
y_pred_ls = m_ls * x + b_ls
y_pred_gd = m_gd * x + b_gd

plt.figure(figsize=(20,10))
plt.scatter(x, y, label='Data points')
plt.plot(x, y_pred_ls, color='red', label='Least Squares Line')
plt.plot(x, y_pred_gd, color='green', label='Gradient Descent Line')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Least Squares vs Gradient Descent')
plt.legend()
plt.show()

print(f"Least Squares: m = {m_ls:.2f}, b = {b_ls:.2f}")
print(f"Gradient Descent: m = {m_gd:.2f}, b = {b_gd:.2f}")


import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample dataset
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
y = np.array([2, 3, 5, 6, 8, 10, 11, 13, 15, 17])

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Train the Linear Regression model
model = LinearRegression()
model.fit(x_train, y_train)

# Plot the data points and regression line
plt.scatter(x, y, color='red', label='Data Points')
plt.plot(x, model.predict(x), color='blue', label='Regression Line')
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression")
plt.legend()
#plt.savefig("linear_regression_output.png")  # Save the image as a file
plt.show()
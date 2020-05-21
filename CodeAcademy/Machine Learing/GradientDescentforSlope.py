# To find the m gradient, or the way the loss changes as the slope of our line changes, we can use this formula:
# we find the sum of x_value * (y_value - (m*x_value + b)) for all the y_values and x_values we have
# and then we multiply the sum by a factor of -2/N. N is the number of points we have.
# import codecademylib3_seaborn
import matplotlib.pyplot as plt

def get_gradient_at_b(x, y, m, b):
    diff = 0
    N = len(x)
    for i in range(N):
        y_val = y[i]
        x_val = x[i]
        diff += (y_val - ((m * x_val) + b))
    b_gradient = -2 / N * diff
    return b_gradient


def get_gradient_at_m(x, y, m, b):
    top = [x_value * (y_value - (m * x_value + b)) for x_value, y_value in zip(x, y)]
    diff = sum(top)
    m_gradient = -2 / len(x) * diff
    return m_gradient


# Define your step_gradient function here
def step_gradient(x, y, b_current, m_current, learning_rate):
    b_gradient = get_gradient_at_b(x, y, b_current, m_current)
    m_gradient = get_gradient_at_m(x, y, b_current, m_current)
    # Let’s try to move the parameter values in the direction of the gradient at a rate of 0.01.
    # 0.01 represents the learning rate
    b = b_current - (learning_rate * b_gradient)
    m = m_current - (learning_rate * m_gradient)
    #   returning the above as a list
    return [b, m]


# Your gradient_descent function here:

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
revenue = [52, 74, 79, 95, 115, 110, 129, 126, 147, 146, 156, 184]


def gradient_descent(x, y, learning_rate, num_iterations):
    b = 0
    m = 0
    for i in range(num_iterations):
        b, m = step_gradient(b, m, x, y, learning_rate)
    return [b, m]


b, m = gradient_descent(months, revenue, 0.01, 1000)

# Lines that plot the result to the browser
y = [m * x + b for x in months]

plt.plot(months, revenue, "o")
plt.plot(months, y)

plt.show()

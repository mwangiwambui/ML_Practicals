# function to calculate gradient descent for loss
def get_gradient_at_b(x, y, m, b):
    result = [(y_value - (m * x_value + b)) for x_value, y_value in zip(x, y)]
    # sum of the above values
    diff = sum(result)
    b_gradient = -2 / len(x) * diff
    return b_gradient

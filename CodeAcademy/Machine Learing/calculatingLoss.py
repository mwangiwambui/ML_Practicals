x = [1, 2, 3]
y = [5, 1, 3]

# y = x
# the slope
m1 = 1
# the y-intercept
b1 = 0
y_predicted1 = [m1 * x_value + b1 for x_value in x]
# y = =0.5x + 1
# the second slope
m2 = 0.5
# the second y-intercept
b2 = 1
y_predicted2 = [m2 * x_value + b2 for x_value in x]
total_loss1 = 0
# iterate through the two lists
for i, j in zip(y, y_predicted1):
    # calculating the difference
    diff = i - j
    # squaring the difference
    diff = diff ** 2
    # adding to total loss1
    total_loss1 = total_loss1 + diff

total_loss2 = 0
# iterate through the two lists
for i, j in zip(y, y_predicted2):
    # calculating the difference
    diff = i - j
    # squaring the difference
    diff = diff ** 2
    # adding to total loss1
    total_loss2 = total_loss2 + diff

print(total_loss1)
print(total_loss2)

better_fit = 2

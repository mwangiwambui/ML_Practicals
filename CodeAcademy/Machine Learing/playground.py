
y_values_of_points = [1, -4, -7, -6]
y_values_of_line = [1, -3, -6, -8]
diff = [(c-a)**2 for c,a in zip(y_values_of_line,y_values_of_points)]
print(sum(diff))
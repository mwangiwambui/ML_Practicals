# equivalent of this using scipy library
# .euclidean()
# .cityblock()

# .hamming() - for this it will divide by the number of points
# from scipy.spatial import distance
def euclidean_distance(pt1, pt2):
    distance = 0
    diff = [(num1 - num2) ** 2 for num1, num2 in zip(pt1, pt2)]
    distance += sum(diff)
    distance = distance ** 0.5
    return distance

# Gets the sum of the absolute difference between the points
def manhattan_distance(pt1, pt2):
    distance = 0
    absol = [abs(num1 - num2) for num1, num2 in zip(pt1, pt2)]
    distance += sum(absol)
    return distance

# Adds one where each value is different
def hamming_distance(pt1, pt2):
    distance = 0
    for i in range(len(pt1)):
        if pt1[i] != pt2[i]:
            distance += 1
    return distance

print(euclidean_distance([1,2], [3,1]))
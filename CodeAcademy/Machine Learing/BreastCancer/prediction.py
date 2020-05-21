# import codecademylib3_seaborn
from sklearn.datasets import load_breast_cancer
# helps us split data to training and validation sets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

breast_cancer_data = load_breast_cancer()
train_test_split(breast_cancer_data.data, breast_cancer_data.target, test_size=0.2, random_state=100)
training_data, validation_data, training_labels, validation_labels = train_test_split(breast_cancer_data.data,
                                                                                      breast_cancer_data.target,
                                                                                      test_size=0.2, random_state=100)
accuracies = []
for k in range(1, 100):
    classifier = KNeighborsClassifier(n_neighbors=k)
    classifier.fit(training_data, training_labels)
    accuracies.append(classifier.score(validation_data, validation_labels))

k_list = range(1, 100)
plt.plot(k_list, accuracies)
plt.xlabel("k")
plt.ylabel("Validation Accuracy")
plt.title("Breast Cancer Classifier Accuracy")
plt.show()


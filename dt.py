# 1. DECISION TREE USING "ENTROPY"
import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the dataset
iris = load_iris()
X = iris.data  # Features
y = iris.target  # Target label

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the decision tree classifier with entropy as the criterion
clf = DecisionTreeClassifier(criterion='entropy')

# Fit the classifier on the training data
clf.fit(X_train, y_train)

# Predict on the test data
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Plot the decision tree
plt.figure(figsize=(12, 8))
plot_tree(clf, feature_names=iris.feature_names, class_names=iris.target_names, filled=True)

# Save the plot as an image
plt.savefig('decision_tree_plot1.png')  # Saves the plot as a PNG file

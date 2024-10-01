#logistic regression
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data for house prices
data = {
    'Squarefoot': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
    'Price': [50000, 52000, 60000, 60600, 70600, 70890, 70900, 71000]
}

df = pd.DataFrame(data)

# Binarize the target variable: 1 if Price > 60000, else 0
df['Price'] = df['Price'].apply(lambda x: 1 if x > 60000 else 0)

print(df)

# Set the target column
X = df[['Squarefoot']]  # We want it to be treated as a DataFrame, i.e., 2D array
y = df['Price']  # Binary classification target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=0)

# Construct Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)  # .fit function is the main thing for training the data

# Let's make some predictions
y_pred = model.predict(X_test)

# Evaluation of our model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(f'Predicted Class (Above Price Threshold): {y_pred}')

# Accepting the square footage input from user
user_input = float(input("Enter the square footage of the house: "))

user_predictions = model.predict([[user_input]])

print(f'Predicted Class for {user_input} square footage: {user_predictions[0]}')

# Sample data for social media engagement
data = {
    'Likes': [100, 150, 200, 250, 300, 350],
    'Comments': [20, 30, 40, 50, 60, 70],
    'Views': [1000, 1500, 2000, 2500, 3000, 3500]
}

df = pd.DataFrame(data)

# Binarize the target variable: 1 if Views > 2000, else 0
df['Views'] = df['Views'].apply(lambda x: 1 if x > 2000 else 0)

print(df)

# Set the target column
X = df[['Likes', 'Comments']]  # We want it to be treated as a DataFrame, i.e., 2D array
y = df['Views']  # Binary classification target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Construct Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)  # .fit function is the main thing for training the data

# Let's make some predictions
y_pred = model.predict(X_test)

# Evaluation of our model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy}')
print(f'Predicted Class (Above View Threshold): {y_pred}')

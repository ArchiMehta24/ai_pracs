#Supervised learning
#Model: Linear regression
import numpy as np
import pandas as pd
#scikit learn library
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
#sample data
# data = {
#     'Squarefoot' : [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200],
#     'Price' : [50000, 52000, 60000, 60600, 70600, 70890, 70900, 71000]
# }
data = {
    'Likes' : [100, 150, 200, 250, 300, 350],
    'Comments' : [20, 30, 40, 50, 60, 70],
    'Views' : [1000, 1500, 2000, 2500, 3000, 3500]
}

df = pd.DataFrame(data)

print(df)
#set the target column
# X = df[['Squarefoot']] #we want it to be treated as data frame, i.e., 2d array
X = df[['Likes', 'Comments']]
y = df['Views'] #we want it to be treated as list
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
#Construct model
model = LinearRegression()
model.fit(X_train, y_train) #.fit function is the main thing for training the data
#Lets make some predictions
y_pred = model.predict(X_test)
#Evaluation of our model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'Predicted Price: {y_pred}')
#accepting the square footage input from user
# user_input = float(input("Enter the square footage of the house: "))

# user_predictions = model.predict([[user_input]])

# print(f'Predicted Price for {user_input} square footage: {user_predictions[0]}')
import pandas as pd
from sklearn.ensemble import VotingRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor

# Load the CSV file as a Pandas DataFrame
data = pd.read_csv('children.csv')

# Split the DataFrame into features and tags
X = data[['weight', 'gender', 'height']]]
y = data['size']]

# Create a list of models
models = [('decision_tree', DecisionTreeRegressor()), 
        ('linear_regression', LinearRegression()), 
        ('k_neighbors', KNeighborsRegressor(n_neighbors=5))
        ]

# Creates an ensemble model with the above models.
model = VotingRegressor(models)

# Train the model with the data
model.fit(X, y)

# Makes a prediction with the model
weight = 50
sex = 0 # 1 represents boy
height = 158
size_predict = model.predict([['weight', 'gender', 'height']])
print(f'For a weight of {weight} kg, a height of {height} cm and a sex male, a size of {size_predict[0]}')
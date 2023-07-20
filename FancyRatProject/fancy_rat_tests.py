from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier
import random
import numpy as np



def random_forest(X, y):
    n_estimators = 100
    forest = []
    for _ in range(n_estimators):
        estimator = DecisionTreeClassifier(random_state=np.random.randint(1000000))
        estimator.fit(X, y)
        forest.append(estimator)
    return forest

X = np.array([0, 0, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]).reshape(1, -1)
y = np.array([0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1])
forest = random_forest(X, y)

random_forest_classifier = RandomForestClassifier(n_estimators=11)
random_forest_classifier.fit(X, y)
predictions = random_forest_classifier.predict(X)
print('Accuracy:', accuracy_score(y, predictions))
print('Recall:', recall_score(y, predictions))
print('F1-score:', f1_score(y, predictions))
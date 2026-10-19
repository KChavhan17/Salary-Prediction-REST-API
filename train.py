import joblib
import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[1.0, 70], [2.0, 80], [3.0, 85], [5.0, 90]])
y = np.array([30000, 42000, 52000, 75000])

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'salary_model.pkl')
print("Model trained and saved as salary_model.pkl")
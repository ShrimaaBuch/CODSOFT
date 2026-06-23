# Import Libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# =========================
# Load Dataset
# =========================

df = pd.read_csv("advertising.csv")

print("First 5 Rows")
print(df.head())

print("\nDataset Information")
print(df.info())

print("\nStatistical Summary")
print(df.describe())


# =========================
# Check Missing Values
# =========================

print("\nMissing Values:")
print(df.isnull().sum())


# =========================
# Data Visualization
# =========================

sns.pairplot(df)
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(), annot=True, cmap="Blues")
plt.title("Correlation Matrix")
plt.show()


# =========================
# Define Features and Target
# =========================

X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']


# =========================
# Split Dataset
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# =========================
# Train Model
# =========================

model = LinearRegression()

model.fit(X_train, y_train)

print("\nModel Trained Successfully")


# =========================
# Prediction
# =========================

y_pred = model.predict(X_test)

print("\nPredicted Sales:")
print(y_pred[:10])


# =========================
# Model Evaluation
# =========================

mae = mean_absolute_error(y_test, y_pred)

mse = mean_squared_error(y_test, y_pred)

rmse = np.sqrt(mse)

r2 = r2_score(y_test, y_pred)

print("\nModel Performance")

print("MAE :", mae)

print("MSE :", mse)

print("RMSE:", rmse)

print("R2 Score:", r2)


# =========================
# Actual vs Predicted
# =========================

results = pd.DataFrame({
    'Actual': y_test,
    'Predicted': y_pred
})

print("\nActual vs Predicted")
print(results.head(10))


# =========================
# Scatter Plot
# =========================

plt.figure(figsize=(8,6))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Sales")

plt.ylabel("Predicted Sales")

plt.title("Actual vs Predicted Sales")

plt.show()


# =========================
# User Prediction
# =========================

tv = float(input("Enter TV Advertisement Budget: "))
radio = float(input("Enter Radio Advertisement Budget: "))
newspaper = float(input("Enter Newspaper Advertisement Budget: "))

prediction = model.predict([[tv, radio, newspaper]])

print("\nPredicted Sales =", prediction[0])
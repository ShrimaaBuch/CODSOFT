# ==========================
# IRIS FLOWER CLASSIFICATION
# ==========================

# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================
# Load Dataset
# ==========================

df = pd.read_csv("Iris.csv")

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# ==========================
# Visualization
# ==========================

plt.figure(figsize=(6,4))
sns.countplot(x="species", data=df)
plt.title("Species Distribution")
plt.show()

# Pair Plot
#sns.pairplot(df, hue="species")
#plt.show()

# Correlation Heatmap
#numeric_data = df.drop("species", axis=1)

#plt.figure(figsize=(6,4))
#sns.heatmap(numeric_data.corr(), annot=True)
#plt.title("Correlation Heatmap")
#plt.show()

# ==========================
# Prepare Data
# ==========================

X = df.drop("species", axis=1)
y = df["species"]

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# Train Model
# ==========================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# ==========================
# Predictions
# ==========================

y_pred = model.predict(X_test)

# ==========================
# Evaluation
# ==========================

accuracy = accuracy_score(y_test, y_pred)

print("\nAccuracy:")
print(accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Plot confusion matrix
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# ==========================
# Test New Flower
# ==========================

sample_flower = [[5.1, 3.5, 1.4, 0.2]]

prediction = model.predict(sample_flower)

print("\nPredicted Species:")
print(prediction[0])
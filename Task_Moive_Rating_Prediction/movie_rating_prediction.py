import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv("IMDb Movies India.csv", encoding="latin1")

# Keep useful columns
df = df[['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3', 'Rating']]

# Remove missing values
df.dropna(inplace=True)

# Convert text columns into numbers
encoder = LabelEncoder()

for column in ['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']:
    df[column] = encoder.fit_transform(df[column])

# Features and Target
X = df[['Genre', 'Director', 'Actor 1', 'Actor 2', 'Actor 3']]
y = df['Rating']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
print("MAE:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Sample prediction
sample = X.iloc[[0]]
predicted_rating = model.predict(sample)

print("Predicted Rating:", predicted_rating[0])
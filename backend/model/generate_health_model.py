# generate_health_model.py

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Step 1: Generate dummy health data
np.random.seed(42)
n = 1000
df = pd.DataFrame({
    'age': np.random.randint(18, 90, n),
    'weight': np.random.uniform(45, 120, n),
    'body_temp': np.random.normal(36.8, 0.4, n),
    'bp_systolic': np.random.randint(90, 180, n),
    'cholesterol': np.random.randint(120, 280, n)
})

# Step 2: Create labels (1 = at risk, 0 = healthy)
df['at_risk'] = (
    (df['bp_systolic'] > 140) |
    (df['cholesterol'] > 240) |
    (df['body_temp'] > 37.5)
).astype(int)

# Step 3: Train a model
X = df[['age', 'weight', 'body_temp', 'bp_systolic', 'cholesterol']]
y = df['at_risk']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 4: Save model to 'health_model.pkl'
joblib.dump(model, 'health_model.pkl')
print("✅ health_model.pkl file generated successfully.")

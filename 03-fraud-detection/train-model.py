# train_model.py
import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("E:/DataSets/creditcard.csv")
X = df.drop(columns=["Time", "Class"])
model = IsolationForest(n_estimators=100, contamination=0.0017, random_state=42)
model.fit(X)

joblib.dump(model, "model/isolation_forest.pkl")
print("Model saved!")

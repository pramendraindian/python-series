#pip install pandas scikit-learn matplotlib seaborn
#pip install pymssql
#pip list
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix

# Step 1: Load dataset
df = pd.read_csv("E:/DataSets/creditcard.csv")  # Path to your downloaded file

# Step 2: Basic infoclscls
print(df['Class'].value_counts())  # 0 = normal, 1 = fraud

# Step 3: Select features (drop Time and Class for training)
X = df.drop(columns=["Time", "Class"])
y_true = df["Class"]
print(X.head())
# Step 4: Train Isolation Forest
model = IsolationForest(n_estimators=100, contamination=0.0017, random_state=42)  # Approx % of fraud in dataset
model.fit(X)

# Step 5: Predict anomalies
y_pred = model.predict(X)
# Convert predictions: 1 -> normal, -1 -> fraud
y_pred = [1 if x == -1 else 0 for x in y_pred]

# Step 6: Evaluation
print("Confusion Matrix:")
print(confusion_matrix(y_true, y_pred))
print("\nClassification Report:")
print(classification_report(y_true, y_pred, digits=4))

# Optional: Visualize with a feature
sns.histplot(df[df["Class"] == 1]["Amount"], bins=50, color='red', label="Fraud")
#sns.histplot(df[df["Class"] == 0]["Amount"], bins=50, color='blue', label="Normal")
plt.legend()
plt.title("Transaction Amount Distribution")
plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import IsolationForest
from sklearn.metrics import classification_report, confusion_matrix

np.random.seed(42)
num_samples = 1000

speed = np.random.normal(loc=60, scale=10, size=num_samples)
brake_status = np.random.choice([0, 1], size=num_samples)  # 0 = no brake, 1 = brake
steering_angle = np.random.normal(loc=0, scale=15, size=num_samples)
sensor_value = np.random.normal(loc=100, scale=5, size=num_samples)

# Create anomaly label (0 = normal, 1 = anomaly)
anomaly = np.zeros(num_samples)

# Introduce artificial anomalies
anomaly_indices = np.random.choice(num_samples, 50, replace=False)

speed[anomaly_indices] = speed[anomaly_indices] + 50
sensor_value[anomaly_indices] = sensor_value[anomaly_indices] + 30

anomaly[anomaly_indices] = 1

data = pd.DataFrame({
    "Speed": speed,
    "Brake_Status": brake_status,
    "Steering_Angle": steering_angle,
    "Sensor_Value": sensor_value,
    "Anomaly": anomaly
})

print(data.head())

X = data[["Speed", "Brake_Status", "Steering_Angle", "Sensor_Value"]]
y = data["Anomaly"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Decision Tree Results:")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

iso = IsolationForest(contamination=0.05, random_state=42)
iso.fit(X)

iso_pred = iso.predict(X)

# Convert output (-1 = anomaly, 1 = normal) to (1 = anomaly, 0 = normal)
iso_pred = np.where(iso_pred == -1, 1, 0)

print("Isolation Forest Results:")
print(confusion_matrix(y, iso_pred))

plt.scatter(data["Speed"], data["Sensor_Value"], c=data["Anomaly"])
plt.xlabel("Speed")
plt.ylabel("Sensor Value")
plt.title("Anomalies in ADAS Log Data")
plt.show()
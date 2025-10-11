# pip install scikit-learn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load real dataset
iris = load_iris()

# Data structures
features = list(iris.feature_names)             # list
classes  = set(iris.target_names)               # set
summary_info = ("Iris", len(features), len(classes))  # tuple

# Split, train, predict
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.3, random_state=42
)
model = LogisticRegression(max_iter=300).fit(X_train, y_train)
y_pred = model.predict(X_test)

# Results in a dict
results = {
    "dataset": summary_info[0],
    "n_features": summary_info[1],
    "n_classes": summary_info[2],
    "accuracy": round(accuracy_score(y_test, y_pred), 3),
}

print("Features (list):", features)
print("Classes (set):", classes)
print("Summary (tuple):", summary_info)
print("Results (dict):", results)



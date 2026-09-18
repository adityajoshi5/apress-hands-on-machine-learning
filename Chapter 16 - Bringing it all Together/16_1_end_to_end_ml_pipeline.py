#!/usr/bin/env python
"""Chapter 16: End-to-end supervised ML pipeline."""

from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd


def main() -> None:
    data = pd.DataFrame(
        {
            "age": [21, 45, 33, 50, 29, 40, 26, 38, 47, 31],
            "salary": [28000, 72000, 43000, 81000, 36000, 62000, 33000, 57000, 75000, 41000],
            "city": ["Pune", "Delhi", "Mumbai", "Delhi", "Pune", "Mumbai", "Pune", "Delhi", "Mumbai", "Pune"],
            "bought": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0],
        }
    )

    x = data[["age", "salary", "city"]]
    y = data["bought"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42, stratify=y)

    preprocessor = ColumnTransformer(
        transformers=[
            (
                "num",
                Pipeline([("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]),
                ["age", "salary"],
            ),
            (
                "cat",
                Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("ohe", OneHotEncoder())]),
                ["city"],
            ),
        ]
    )

    model = Pipeline([("prep", preprocessor), ("clf", LogisticRegression(max_iter=2000))])
    model.fit(x_train, y_train)

    preds = model.predict(x_test)
    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print("F1 score:", round(f1_score(y_test, preds), 4))


if __name__ == "__main__":
    main()

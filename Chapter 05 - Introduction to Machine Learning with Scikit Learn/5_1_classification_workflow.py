#!/usr/bin/env python
"""Chapter 05: Basic scikit-learn classification workflow."""

from sklearn.datasets import load_wine
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split


def main() -> None:
    wine = load_wine()
    x_train, x_test, y_train, y_test = train_test_split(
        wine.data, wine.target, test_size=0.25, random_state=42, stratify=wine.target
    )

    model = LogisticRegression(max_iter=5000)
    model.fit(x_train, y_train)
    preds = model.predict(x_test)

    print("Accuracy:", round(accuracy_score(y_test, preds), 4))
    print("\nClassification report:\n", classification_report(y_test, preds, target_names=wine.target_names))


if __name__ == "__main__":
    main()

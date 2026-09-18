#!/usr/bin/env python
"""Chapter 09: Support Vector Machine and Naive Bayes examples."""

from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC


def main() -> None:
    digits = load_digits()
    x_train, x_test, y_train, y_test = train_test_split(
        digits.data, digits.target, test_size=0.2, random_state=21, stratify=digits.target
    )

    models = {
        "SVM": SVC(kernel="rbf", gamma="scale", C=5),
        "GaussianNB": GaussianNB(),
    }

    for name, model in models.items():
        model.fit(x_train, y_train)
        preds = model.predict(x_test)
        print(f"{name} accuracy: {accuracy_score(y_test, preds):.4f}")


if __name__ == "__main__":
    main()

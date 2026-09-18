#!/usr/bin/env python
"""Chapter 07: Compare KNN and Decision Tree classifiers."""

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier


def main() -> None:
    dataset = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(
        dataset.data, dataset.target, test_size=0.2, random_state=11, stratify=dataset.target
    )

    knn = KNeighborsClassifier(n_neighbors=7)
    tree = DecisionTreeClassifier(max_depth=4, random_state=11)

    for name, model in [("KNN", knn), ("Decision Tree", tree)]:
        model.fit(x_train, y_train)
        preds = model.predict(x_test)
        print(f"{name} accuracy: {accuracy_score(y_test, preds):.4f}")


if __name__ == "__main__":
    main()

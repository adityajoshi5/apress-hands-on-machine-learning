#!/usr/bin/env python
"""Chapter 08: Hyperparameter tuning using GridSearchCV."""

from sklearn.datasets import load_wine
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.svm import SVC


def main() -> None:
    wine = load_wine()
    x_train, x_test, y_train, y_test = train_test_split(
        wine.data, wine.target, test_size=0.2, random_state=7, stratify=wine.target
    )

    grid = {
        "C": [0.1, 1, 10],
        "kernel": ["linear", "rbf"],
        "gamma": ["scale", "auto"],
    }

    search = GridSearchCV(SVC(), param_grid=grid, cv=5, n_jobs=-1)
    search.fit(x_train, y_train)

    print("Best params:", search.best_params_)
    print("Best CV score:", round(search.best_score_, 4))
    print("Test score:", round(search.score(x_test, y_test), 4))


if __name__ == "__main__":
    main()

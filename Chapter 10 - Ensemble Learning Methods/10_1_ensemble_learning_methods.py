#!/usr/bin/env python
"""Chapter 10: Ensemble methods for classification."""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split


def main() -> None:
    data = load_breast_cancer()
    x_train, x_test, y_train, y_test = train_test_split(
        data.data, data.target, test_size=0.25, random_state=19, stratify=data.target
    )

    models = {
        "RandomForest": RandomForestClassifier(n_estimators=200, random_state=19),
        "GradientBoosting": GradientBoostingClassifier(random_state=19),
    }

    for name, model in models.items():
        model.fit(x_train, y_train)
        prob = model.predict_proba(x_test)[:, 1]
        print(f"{name} ROC-AUC: {roc_auc_score(y_test, prob):.4f}")


if __name__ == "__main__":
    main()

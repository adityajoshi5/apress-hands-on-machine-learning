#!/usr/bin/env python
"""Chapter 06: Data preparation with imputing, scaling, and encoding."""

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def main() -> None:
    data = pd.DataFrame(
        {
            "age": [24, 29, None, 42, 35],
            "income": [32000, 45000, 39000, None, 52000],
            "city": ["Pune", "Delhi", "Pune", "Mumbai", None],
        }
    )

    num_features = ["age", "income"]
    cat_features = ["city"]

    numeric_pipeline = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )
    categorical_pipeline = Pipeline(
        steps=[("imputer", SimpleImputer(strategy="most_frequent")), ("encoder", OneHotEncoder())]
    )

    preprocessor = ColumnTransformer(
        transformers=[("num", numeric_pipeline, num_features), ("cat", categorical_pipeline, cat_features)]
    )

    transformed = preprocessor.fit_transform(data)
    print("Original data:\n", data)
    print("\nTransformed shape:", transformed.shape)


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Chapter 04: Introductory pandas DataFrame manipulations."""

import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "student": ["Asha", "Brian", "Carlos", "Dina", "Ethan"],
            "math": [88, 75, 93, 67, 81],
            "science": [91, 70, 89, 73, 78],
            "attendance": [0.95, 0.87, 0.98, 0.8, 0.9],
        }
    )

    df["avg_score"] = df[["math", "science"]].mean(axis=1)
    top_students = df.sort_values("avg_score", ascending=False).head(3)
    low_attendance = df[df["attendance"] < 0.9]

    print("Full DataFrame:\n", df)
    print("\nTop students:\n", top_students[["student", "avg_score"]])
    print("\nStudents below 90% attendance:\n", low_attendance[["student", "attendance"]])


if __name__ == "__main__":
    main()

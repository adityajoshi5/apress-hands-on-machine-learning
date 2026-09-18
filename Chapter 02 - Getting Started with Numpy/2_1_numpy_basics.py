#!/usr/bin/env python
"""Chapter 02: Numpy fundamentals and vectorized operations."""

import numpy as np


def main() -> None:
    sales = np.array([1200, 1500, 1350, 1700, 1600], dtype=float)
    expenses = np.array([500, 620, 590, 700, 650], dtype=float)

    profit = sales - expenses
    growth_rate = (sales[1:] - sales[:-1]) / sales[:-1]

    matrix = np.array(
        [
            [1.0, 2.0, 3.0],
            [4.0, 5.0, 6.0],
            [7.0, 8.0, 9.0],
        ]
    )

    normalized = (matrix - matrix.mean(axis=0)) / matrix.std(axis=0)

    print("Sales:", sales)
    print("Profit per month:", profit)
    print("Average profit:", round(float(profit.mean()), 2))
    print("Monthly growth rate (%):", np.round(growth_rate * 100, 2))
    print("Matrix shape:", matrix.shape)
    print("Normalized matrix:\n", np.round(normalized, 3))


if __name__ == "__main__":
    main()

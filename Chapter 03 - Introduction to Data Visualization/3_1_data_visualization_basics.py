#!/usr/bin/env python
"""Chapter 03: Basic data visualization examples with matplotlib."""

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    epochs = np.arange(1, 11)
    train_loss = np.array([1.2, 1.0, 0.85, 0.72, 0.63, 0.57, 0.51, 0.48, 0.45, 0.42])
    val_loss = np.array([1.25, 1.08, 0.95, 0.82, 0.77, 0.72, 0.71, 0.69, 0.7, 0.72])

    fig, axes = plt.subplots(1, 2, figsize=(11, 4))

    axes[0].plot(epochs, train_loss, marker="o", label="Train Loss")
    axes[0].plot(epochs, val_loss, marker="s", label="Validation Loss")
    axes[0].set_title("Training vs Validation Loss")
    axes[0].set_xlabel("Epoch")
    axes[0].set_ylabel("Loss")
    axes[0].legend()
    axes[0].grid(alpha=0.2)

    accuracy = np.array([62, 68, 72, 76, 80, 82, 84, 85, 86, 87])
    axes[1].bar(epochs, accuracy, color="tab:green")
    axes[1].set_title("Accuracy by Epoch")
    axes[1].set_xlabel("Epoch")
    axes[1].set_ylabel("Accuracy (%)")
    axes[1].set_ylim(50, 100)

    plt.tight_layout()
    output_path = "chapter03_loss_accuracy_plot.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    print(f"Saved visualization to {output_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python
"""Chapter 13: Feedforward neural network on synthetic data."""

import torch


def make_dataset(n_samples: int = 400):
    x = torch.randn(n_samples, 4)
    y = (x[:, 0] + 0.8 * x[:, 1] - 0.5 * x[:, 2] > 0).long()
    return x, y


def main() -> None:
    x, y = make_dataset()

    model = torch.nn.Sequential(
        torch.nn.Linear(4, 16),
        torch.nn.ReLU(),
        torch.nn.Linear(16, 8),
        torch.nn.ReLU(),
        torch.nn.Linear(8, 2),
    )

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for _ in range(150):
        logits = model(x)
        loss = criterion(logits, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    preds = model(x).argmax(dim=1)
    accuracy = (preds == y).float().mean().item()

    print("Training loss:", round(float(loss.item()), 6))
    print("Training accuracy:", round(accuracy, 4))


if __name__ == "__main__":
    main()

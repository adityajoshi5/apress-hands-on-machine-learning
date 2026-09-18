#!/usr/bin/env python
"""Chapter 14: Convolutional neural network for toy image classification."""

import torch


def main() -> None:
    x = torch.randn(256, 1, 8, 8)
    y = (x.mean(dim=(1, 2, 3)) > 0).long()

    model = torch.nn.Sequential(
        torch.nn.Conv2d(1, 8, kernel_size=3, padding=1),
        torch.nn.ReLU(),
        torch.nn.MaxPool2d(2),
        torch.nn.Conv2d(8, 16, kernel_size=3, padding=1),
        torch.nn.ReLU(),
        torch.nn.Flatten(),
        torch.nn.Linear(16 * 4 * 4, 2),
    )

    criterion = torch.nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

    for _ in range(80):
        logits = model(x)
        loss = criterion(logits, y)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

    acc = (model(x).argmax(dim=1) == y).float().mean().item()
    print("Final loss:", round(float(loss.item()), 6))
    print("Training accuracy:", round(acc, 4))


if __name__ == "__main__":
    main()

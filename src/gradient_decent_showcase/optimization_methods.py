from collections.abc import Callable

import numpy
import torch
from numpy.typing import NDArray


def gradient_decent(
    step_size: float,
    grad_fn: Callable,
    x0: tuple[float, float],
    max_iters: int = 2000,
    tol: float = 1e-6,
) -> NDArray:
    x = torch.tensor(x0, dtype=torch.float64)
    path = [x.clone()]

    for _ in range(max_iters):
        grad = grad_fn(x)
        x_next = x - step_size * grad
        path.append(x_next.clone())

        if torch.linalg.norm(x_next - x) < tol:
            break

        x = x_next

    return numpy.array(path)

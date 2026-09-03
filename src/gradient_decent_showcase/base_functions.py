import torch


def convex_bowl_torch(xy: torch.Tensor) -> torch.Tensor:
    return torch.sum(xy**2)


def banana_valley_torch(xy: torch.Tensor) -> torch.Tensor:
    x, y = xy
    return (1 - x) ** 2 + 100 * (y - x**2) ** 2


def cosine_bumps_torch(xy: torch.Tensor) -> torch.Tensor:
    x, y = xy
    return x**2 + y**2 + 10 * torch.cos(x) + 10 * torch.cos(y)

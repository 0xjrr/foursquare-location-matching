import os
import hydra
import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
from tqdm import tqdm
from dataclasses import dataclass


@dataclass
class ConfigVars:
    seed_number: int
    train_set: str
    test_set: str
    target_col: str


def main() -> None:
    pass


if __name__ == '__main__':
    main()
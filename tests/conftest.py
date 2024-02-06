# Pytest Fixtures defined in this file are accessible in all other tests
# without needing to import them: https://docs.pytest.org/en/7.1.x/reference/fixtures.html#conftest-py-sharing-fixtures-across-multiple-files

from pathlib import Path

import pandas as pd
import pytest


@pytest.fixture
def example_csv_file(tmp_path: Path) -> Path:
    """
    Creates an example csv file in a temporary path, suitable for  testing
    `read_raw_data()`

    Uses the pytest tmp_path fixture: https://docs.pytest.org/en/7.1.x/reference/reference.html#std-fixture-tmp_path
    """

    df = pd.DataFrame({"Order": [0, 1, 2], "column1": [1, 2, 3], "column2": [4, 5, 6]})

    target_path = tmp_path / "example.csv"

    df.to_csv(target_path, sep="\t")

    return target_path

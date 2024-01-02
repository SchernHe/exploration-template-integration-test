from pathlib import Path

import pandas as pd
import pandera
import pandera.typing

from .schemas import RawDataSchema


def read_raw_data(p: Path) -> pd.DataFrame:
    """Preconfigured way to open our raw data.
    As soon as custom logic is necessary to open data (in this case: `index_col`), put
    it in its own function.

    Parameters
    ----------
    p : Path
            Path to the file.

    Returns
    -------
    pd.DataFrame
            Dataframe with "Order" as the index.
    """
    df = pd.read_csv(p, index_col="Order", sep="\t")

    return df


# `lazy=True` means that it checks for all errors, instead of failing on the first one
@pandera.check_types(lazy=True)
def read_raw_data_with_schema(p: Path) -> pandera.typing.DataFrame[RawDataSchema]:
    """Alternative function to `read_raw_data`.
    Reads raw data from the path and checks whether the
    [RawDataSchema][integration_test_instance.io.schemas.RawDataSchema] is followed.

    Parameters
    ----------
    p : Path
            Path to the raw data file

    Returns
    -------
    pandera.typing.DataFrame[RawDataSchema]
            Dataframe with the schema checked
    """
    raw_data = read_raw_data(p)

    raw_pandera_data = pandera.typing.DataFrame[RawDataSchema](raw_data)

    return raw_pandera_data

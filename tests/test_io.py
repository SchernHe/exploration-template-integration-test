from pathlib import Path

from integration_test_instance import io


def test_read_raw_data(example_csv_file: Path) -> None:
    df = io.read_raw_data(example_csv_file)

    assert df.index.name == "Order", "Index column isn't called 'Order'"
    assert len(df) == 3, f"Unexpected amount of columns: {len(df)=}"

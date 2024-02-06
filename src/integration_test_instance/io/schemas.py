import pandera as pa
from pandera.typing import Index, Series


class RawDataSchema(pa.SchemaModel):
    """InputSchema, used in [RAW_DATA_FILE][integration_test_instance.constants.RAW_DATA_FILE]"""

    order: Index[int] = pa.Field(alias="Order", ge=0, check_name=True, unique=True)
    """Observation number."""
    pid: Series[int] = pa.Field(alias="PID", unique=True, gt=0)
    """Parcel identification number - can be used with city web site for parcel review."""
    sale_price: Series[int] = pa.Field(alias="SalePrice", gt=0)
    """The sale price of the property"""
    street: Series[str] = pa.Field(alias="Street", isin=["Pave", "Grvl"])
    """Type of road access to property. Either `Pave` or `Grvl`"""
    fence: Series[str] = pa.Field(alias="Fence", nullable=True)
    """Fence quality, can be `NaN`"""

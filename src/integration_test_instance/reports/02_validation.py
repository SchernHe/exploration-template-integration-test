# %% [markdown]
#
# # 2) Data Validation
#
# Any findings and assumptions formulated based on the data exploration should be
# encoded and validated automatically.
#
# This supports the [MLOps principles](../../#goal-of-this-template) in the following way:
#
# - Decisions regarding data descriptions are auditable via Git
# - Collaborating is easier due to the explicit documentation
# - Assumptions formed during the early phases of a project are continuously validated
#
# This notebook shows two ways to do this:
#
# - A) Via `assert` statements
# - B) Via [pandera](https://pandera.readthedocs.io)

# %%
from integration_test_instance import constants, io
from integration_test_instance.constants import PROJECT_ROOT

print(PROJECT_ROOT)
# %%
raw_df = io.read_raw_data(constants.RAW_DATA_FILE)

# %% [markdown]
#
# ## A) Via `assert` statements
#
# The most barebones solution to validate assumptions about the data.
# This report will fail during execution time, if the assumptions don't hold true anymore

# %%
assert raw_df["PID"].dtype == "int64"
assert raw_df["Street"].apply(lambda x: x in {"Grvl", "Pave"}).all()

# %% [markdown]
#
# ## B) Via [pandera](https://pandera.readthedocs.io)
#
# Pandera is a library designed both for schema validation (i.e., which columns are
# present and what datatype do they have), as well as value checking (are the values in
# an expected range, are `NaN`s present, do they have a minimum variance)

# %%

from integration_test_instance.io.schemas import RawDataSchema

RawDataSchema.validate(raw_df)

# %% [markdown]

# Instead of manually validating via `RawDataSchema.validate(...)`,
# pandera also offers [decorators](https://pandera.readthedocs.io/en/stable/decorators.html), which can be directly applied to the IO functions.
#
# See [the reference for `integration_test_instance.io.read_raw_data_with_schema`](../../reference//#integration_test_instance.io.read_raw_data_with_schema):

# %%
from integration_test_instance.io import read_raw_data_with_schema

raw_data_with_schema = read_raw_data_with_schema(constants.RAW_DATA_FILE)

# %% [markdown]
#
# The individual attributes of the schema have their docstrings attached:
#
# ![schema docstring image](../../images/schema_docstring.png)
#
# Additionally, the schema documentation is part of the [code reference](../../reference#integration_test_instance.io.schemas.RawDataSchema).
#

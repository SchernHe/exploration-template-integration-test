# %% [markdown]
# # 1) Raw Data Exploration
# This shows how a Python file formatted with [jupytext](https://pypi.org/project/jupytext/)
# can be used to generate traceable reports

# %% [markdown]
"""
## Development Setup Tips

Automatically reload imported packages, so that you can develop in your
python package and import any changes you made, without having to
restart the kernel,
see [here](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html#autoreload).

Since jupytext doesn't support the `%`-magic format, we have to call the magic slightly
differently:
"""
# %%
from IPython import get_ipython

if ipython := get_ipython():
    # If we're in an ipython environment, set the magic
    ipython.run_line_magic("load_ext", line="autoreload")
    ipython.run_line_magic("autoreload", line="all")

# %%
from integration_test_instance.constants import PROJECT_ROOT

print(PROJECT_ROOT)
# %% [markdown]
"""
## Data Exploration

Here's how an initial data exploration could look like:

"""
# %%
from integration_test_instance import constants, io

# %%
constants.RAW_DATA_FILE

# %%
raw_df = io.read_raw_data(constants.RAW_DATA_FILE)
# %%
raw_df.head()

# %%
raw_df.describe()

# %%

raw_df.columns

# %%

import seaborn as sns

sns.relplot(data=raw_df, x="Year Built", y="SalePrice")

# %%

import plotly.express as px
import plotly.io as pio

pio.renderers.default = "plotly_mimetype+sphinx_gallery"
px.scatter_3d(raw_df, x="Year Built", y="SalePrice", z="Lot Area", color="House Style")

# %% [markdown]

# ## Data Validation
# During the data exploration, it makes sense to formulate assumptions about the data,
# e.g. that there are no `NaN`s present, or that a certain column only contains value
# from a specific set.
#
# The simplest way to do this is via `assert` statements.
# If these assumptions are written in code, then this report
# will fail during execution and therefore warn you if in the future these
# assumptions don't hold true anymore.
#

# %%
assert raw_df["PID"].dtype == "int64"
assert raw_df["Street"].apply(lambda x: x in {"Grvl", "Pave"}).all()

# %% [markdown]
# ## Export of this report
#
# To export this report, simply use the "Save Page" or "Print Page" feature of your browser.
# Although some tools exist to export these pages, so far our exploration didn't find a
# better fitting solution than using your browser.

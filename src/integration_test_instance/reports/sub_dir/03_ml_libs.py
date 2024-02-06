# %% [markdown]
# # 3) ML Libs
#
# This notebook just verifies that the ML libs can be imported

# %%
try:
    import tensorflow as tf

    tf.__version__
except ModuleNotFoundError:
    print(
        """Tensorflow couldn't be imported, probably it wasn't selected as dependency
    during the instantiation of the template."""
    )

# %%
try:
    import torch

    torch.__version__
except ModuleNotFoundError:
    print(
        """Pytorch couldn't be imported, probably it wasn't selected as dependency
    during the instantiation of the template."""
    )

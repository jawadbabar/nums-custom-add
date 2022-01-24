import nums.core.settings as settings
from nums.core.application_manager import instance
from nums.core.array.blockarray import BlockArray, Block
from nums.core.array.application import ArrayApplication

import ray


# useful function to flatten a list of list
def flatten(t):
    return [item for sublist in t for item in sublist]


def test_custom_add():
    app: ArrayApplication = instance()

    X = app.random.normal(loc=1.0, scale=10.0, shape=(100,), block_shape=(23,))
    Y = app.random.normal(loc=1.0, scale=10.0, shape=(100,), block_shape=(23,))

    Z1 = X + Y
    Z2 = X.custom_add_wrapper(Y)

    Z1_GET = Z1.get()
    Z2_GET = flatten(ray.get(ray.get([Z2.blocks[grid_entry].oid for grid_entry in Z2.grid.get_entry_iterator()])))

    for default, custom in zip(Z1_GET, Z2_GET):
        assert default == custom

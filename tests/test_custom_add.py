from nums.core.application_manager import instance
from nums.core.array.application import ArrayApplication


def test_custom_add():
    app: ArrayApplication = instance()

    X = app.random.normal(loc=1.0, scale=10.0, shape=(100,), block_shape=(23,))
    Y = app.random.normal(loc=1.0, scale=10.0, shape=(100,), block_shape=(23,))

    Z1 = X + Y
    Z2 = X.add_wrapper(Y)

    for default, custom in zip(Z1.get(), Z2.get()):
        assert default == custom

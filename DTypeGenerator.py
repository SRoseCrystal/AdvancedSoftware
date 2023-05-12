import numpy as np

class DTypeGenerator(np.random.Generator):
    def normal(self, loc=0.0, scale=1.0, size=None, dtype=None):
        if dtype is None:
            return super().normal(loc=loc, scale=scale, size=size)
        else:
            return super().normal(loc=loc, scale=scale, size=size).astype(dtype)
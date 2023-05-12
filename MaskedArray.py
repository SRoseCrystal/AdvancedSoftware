import numpy as np
from numpy.ma import MaskedArray

class MyMaskedArray(MaskedArray):
    def __array_function__(self, func, types, args, kwargs):
        if func == np.append:
            # Custom logic for np.append with MaskedArray
            # Modify or fix the behavior here
            return super().__array_function__(func, types, args, kwargs)

        # For other functions, delegate to the parent class
        return super().__array_function__(func, types, args, kwargs)

# Create a MaskedArray object
a = MyMaskedArray([1, 2, 3], mask=[False, True, False])

# Use np.append with the custom MaskedArray object
result = np.append(a, 4)
print(result)

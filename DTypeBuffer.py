import numpy as np

# Define the new-style custom dtype
my_dtype = np.dtype([('x', np.int32), ('y', np.float64), ('z', np.uint8)])

# Create a numpy array of the custom dtype
data = np.array([(1, 2.0, 3), (4, 5.0, 6)], dtype=my_dtype)

# Export the buffer as a void* buffer with encoded dtype information
buf = data.tobytes(order='C')
format_string = f"{data.dtype.char}{data.itemsize}"

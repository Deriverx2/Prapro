import numpy as np
import time

if __name__ == '__main__':
    start_time = time.time()
    array = np.random.rand(1000,1000) # Generate a 1000x1000 array of random numbers
    end_time = time.time()
    print(array)
    total_time = end_time - start_time
    print(f"Time taken: {total_time} seconds" )
    
    # Convert the array to a byte array
    byte_array = np.frombuffer(array, dtype=np.byte)
    print(byte_array)

    # Convert the byte array back to the original array
    original_array = np.frombuffer(byte_array, dtype=np.float64)
    original_array=original_array.reshape(1000,1000)
    if np.array_equal(array, original_array):
        print("The original array is the same as the byte converted array")
    print(original_array)

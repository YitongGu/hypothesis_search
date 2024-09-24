
from typing import List
import numpy as np
from scipy.ndimage import label, find_objects
from scipy.signal import convolve2d
from scipy import ndimage
from collections import Counter
import math
np.int = int



import numpy as np

def transform_grid(input_grid: np.ndarray) -> np.ndarray:
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols))
    
    for i in range(rows):
        for j in range(cols):
            if input_grid[i, j]!= 0:
                output_grid[i, j] = input_grid[i, j]
            else:
                output_grid[i, j] = 0
    
    return output_grid
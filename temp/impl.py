
from typing import List
import numpy as np
from scipy.ndimage import label, find_objects
from scipy.signal import convolve2d
from scipy import ndimage
from collections import Counter
import math
np.int = int

assistant

import numpy as np

def transform_grid(input_grid: np.ndarray) -> np.ndarray:
    rows, cols = input_grid.shape
    output_grid = np.zeros((rows, cols), dtype=int)
    
    for i in range(rows-1):
        output_grid[i] = input_grid[i+1]
    output_grid[rows-1] = 0
    
    return output_grid
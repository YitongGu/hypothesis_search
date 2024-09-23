
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
    color = input_grid[0][0]
    output_grid = np.zeros_like(input_grid)
    for i in range(input_grid.shape[0]):
        for j in range(input_grid.shape[1]):
            if i == 0:
                output_grid[i][j] = color
            else:
                output_grid[i][j] = input_grid[i-1][j]
    return output_grid
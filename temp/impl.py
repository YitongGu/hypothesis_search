
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
    output_grid = input_grid.copy()
    for i in range(1, input_grid.shape[0] - 1):
        for j in range(1, input_grid.shape[1] - 1):
            if input_grid[i, j]!= 0:
                output_grid[i, j] = input_grid[i-1, j]
    return output_grid
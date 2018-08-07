
"""
Arange returns evenly spaced values within a given interval. Along with a starting and stopping point, y
ou can also define a step size or data type if necessary. Note that the stopping point is a ‘cut-off’ value,
so it will not be included in the array output.
"""

import numpy as np


# np.arange(start, stop, step)
np.arange(3, 7, 2)

"""
Linspace is very similar, but with a slight twist. Linspace returns evenly spaced numbers over a specified interval. 
So given a starting and stopping point, as well as a number of values, linspace will evenly space them out 
for you in a NumPy array. This is especially helpful for data visualizations and declaring axes when plotting.
"""

# np.linspace(start, stop, num)
np.linspace(2.0, 3.0, num=5)
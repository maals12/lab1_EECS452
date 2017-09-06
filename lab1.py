import numpy as np
def fn(input):
    tr = np.transpose(input)
    return np.dot(tr, tr[0])


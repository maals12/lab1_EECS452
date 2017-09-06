import numpy as np
def fn(input):
    tran = np.transpose(input)
    return np.dot(tran, tran[0])


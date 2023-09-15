import numpy as np
cimport numpy as np
import cython
cimport cython

cdef extern from "argsort.h":
    cdef void argsort(unsigned long *pidx, double *parr, unsigned long length) nogil

@cython.boundscheck(False)
@cython.wraparound(False)
def pargsort(np.ndarray arr):
    cdef unsigned long l = arr.shape[0]
    cdef double[:] arr2 = arr.astype(np.double)
    cdef unsigned long[:] idx2 = np.arange(l, dtype=np.uint)
    argsort(&idx2[0], &arr2[0], l) # c++ consider memview as a pointer
    return np.asarray(idx2)


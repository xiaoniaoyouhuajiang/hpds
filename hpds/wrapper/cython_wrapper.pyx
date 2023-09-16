""" Small Cython file to demonstrate the use of PyArray_SimpleNewFromData
in Cython to create an array from already allocated memory.
Cython enables mixing C-level calls and Python-level calls in the same
file with a Python-like syntax and easy type cohersion. See 
http://cython.org for more information
"""

# Author: Gael Varoquaux
# License: BSD

# Declare the prototype of the C function we are interested in calling
cdef extern from "c_code.c":
    int *compute(int size)

from libc.stdlib cimport free
from cpython cimport PyObject, Py_INCREF

# Import the Python-level symbols of numpy
import numpy as np

# Import the C-level symbols of numpy
cimport numpy as np

# Numpy must be initialized. When using numpy from C or Cython you must
# _always_ do that, or you will have segfaults
np.import_array()

# We need to build an array-wrapper class to deallocate our array when
# the Python object is deleted.

cdef class ArrayWrapper:
    cdef void* data_ptr
    cdef int size
    cdef int typenum

    cdef set_data(self, int size, void* data_ptr, int typenum):
        """ Set the data of the array
        This cannot be done in the constructor as it must recieve C-level
        arguments.
        Parameters:
        -----------
        size: int
            Length of the array.
        data_ptr: void*
            Pointer to the data.
        typenum: int
            Data type of the array.
        """
        self.data_ptr = data_ptr
        self.size = size
        self.typenum = typenum

    def __array__(self):
        """ Here we use the __array__ method, that is called when numpy
            tries to get an array from the object."""
        cdef np.npy_intp shape[1]
        shape[0] = <np.npy_intp> self.size
        # Create a 1D array, of length 'size'
        ndarray = np.PyArray_SimpleNewFromData(1, shape, self.typenum,
                                               self.data_ptr)
        np.set_array_base(ndarray, self)
        return ndarray

    def __dealloc__(self):
        """ Frees the array. This is called by Python when all the
        references to the object are gone. """
        free(<void*>self.data_ptr)

cdef wrap_int(int size, int* data):
    cdef ArrayWrapper obj = ArrayWrapper()
    obj.set_data(size, <void*>data, np.NPY_INT)
    return np.array(obj, copy=False)

def py_compute(int size):
    """ Python binding of the 'compute' function in 'c_code.c' that does
        not copy the data allocated in C.
    """
    cdef int *array
    # Call the C function
    array = compute(size)

    return wrap_int(size, array)
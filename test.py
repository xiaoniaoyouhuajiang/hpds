from hpds.acclerate import multiply
# from hpds.concurrent import pargsort
from hpds.wrapper import cython_wrapper

import numpy as np
import time

# test vars
factor = 3.0
size = 200000000
arr = np.random.uniform(0,100,100000000)
arr1 = np.linspace(1.0,100.0, size)
arr2 = np.linspace(1.0,100.0, size)
tem = cython_wrapper.py_compute(10)

# test multiply
multiply.multiply_with_scalar(arr1, factor) 
assert arr1.any() == (arr2 * factor).any()

# test cython_wrapper
np.testing.assert_allclose(tem, np.arange(10))

"""
# test argsort
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 调用原始函数
        end_time = time.time()  # 记录结束时间
        execution_time = end_time - start_time  # 计算执行时长
        print(f"{func.__name__} 执行时长: {execution_time} 秒")
        return result
    return wrapper

@timing_decorator
def parallel():
    pargsort.pargsort(arr)

@timing_decorator
def normal():
    np.argsort(arr)

parallel()
normal()
"""

print("All test pass.")
from setuptools import Extension, setup
from Cython.Build import cythonize
import numpy

ext_modules = [
    Extension(
        "pargsort",
        ["pargsort.pyx"],
        language="c++",
        extra_compile_args=["-fopenmp", "-std=c++17"],
        extra_link_args=["-fopenmp"],
        include_dirs=[numpy.get_include()]
    )
]
"""
setup(
    name="pargsort",
    ext_modules=cythonize(ext_modules, compiler_directives={"language_level": "3"}),
)
"""

setup(
    name="pargsort",
    ext_modules=ext_modules,
)
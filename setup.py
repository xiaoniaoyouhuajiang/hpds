from Cython.Build import cythonize
from Cython.Distutils import build_ext
import numpy
from setuptools import Extension, setup

# prepare ext_modules
ext_modules = [
    Extension(
        "pargsort",["./hpds/concurrent/argsort/pargsort.pyx"],
        language="c++", extra_compile_args=["-fopenmp", "-std=c++17"],
        extra_link_args=["-fopenmp"],include_dirs=[numpy.get_include()]
    ),
    Extension(
        "cython_wrapper", ["./hpds/wrapper/cython_wrapper.pyx"],
        depends=['c_code.c'], include_dirs=[numpy.get_include()]
    )
]

with open("README.md", "r", encoding="utf8") as rm:
    readme = rm.read()

if __name__ == '__main__':
    setup(
        name="hpds",
        version="0.0.1",
        description="high performance data structure tool-set for python",
        packages=["hpds"],
        # install_requires=requirements,
        long_description=readme,
        include_package_data=True,
        long_description_content_type="text/markdown",
        author="xiaoniaoyouhuajiang",
        author_email="2583473505@qq.com",
        cmdclass={"build_ext": build_ext},
        license="MIT",
        classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        ],
        ext_modules=ext_modules,
    )
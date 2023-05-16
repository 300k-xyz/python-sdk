import os
import setuptools

setuptools.setup(
    name="tkpysdk",
    version="0.0.1",
    description="300k sdk for python",
    author="Hao W",
    license="Copyright 2023, 300k ltd, All rights reserved",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src')
)

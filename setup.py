"""#############################################################################
setup.py
================================================================================
setuptools setup script for pfpp.
#############################################################################"""
from setuptools import find_packages, setup

# ------------------------------------------------------------------------------
DESCRIPTION = (
    'Library for working with the book "Patterns for Parallel'
    ' Programming", by Mattson, Sanders, and Massingill'
)

setup(
    name="pfpp",
    version="0.1",
    description=DESCRIPTION,
    url="https://github.com/kilicomu/pfpp",
    author="Killian Murphy",
    author_email="murphyklc@gmail.com",
    packages=find_packages(),
    license="WTFPL",
    classifiers=["License :: Public Domain"],
)

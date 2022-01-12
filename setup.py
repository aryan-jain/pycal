from setuptools import find_packages, setup
from setuptools.command.install import install

version = "0.0.1"

setup(
    name="pycal",
    version=version,
    description="pyCal is a simple python service to manage calendar schedules for tasks in python.",
    author="ajain",
    author_email="aryan.jain@livereachmedia.com",
    python_requires=">=3.6, <4",
    packages=find_packages(),
    install_requires=[],
    zip_safe=False,
)

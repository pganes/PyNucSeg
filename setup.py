from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='PyNucSeg',
    version='0.0.1',
    description='A python package for segmentation of fluorescent nucleus, and measure the area of nucleus and the mean intensity per nucleus. This package uses stardist(https://github.com/stardist/stardist) for segmentation and napari(https://github.com/napari/napari) for visualization.',
    py_modules=['pynucseg'],
    package_dir={'':'pynucseg'},
    classifiers=[
    "Programming Language :: Python :: 3.10",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown", 
    install_requires=[
    "numpy",
    "stardist",
    "napari",
    "scikit-image",
    "tensorflow",
    ],
    extras_require ={
    "dev": [
    "pytest>=3.7",
    "twine",
    ]
    },
    url="https://github.com/pganes/PyNucSeg",
    author="Ganesh Pandey",
    author_email="gpande3@uic.edu",

)
from setuptools import setup

# read the contents of the README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="chemplot", 
    version="0.1.0",
    author="Murat Cihan Sorkun",
    author_email="m.c.sorkun@differ.nl",
    description="A python library for chemical space visualization.",
    long_description=long_description,
    long_description_content_type='text/markdown'
    url="https://github.com/mcsorkun/ChemPlot",
    license="BSD",
    packages=["chemplot"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Topic :: Scientific/Engineering"
    ],
    keywords="chemoinformatics dimension reduction",
    install_requires=[
        "numpy >= 1.17",
        "mordred >= 1.2.0",
        "pandas >= 1.0.1",
        "scikit-learn >= 0.22",
        "umap-learn >= 0.4.5",
        "seaborn >= 0.11.0",
        "scipy >= 1.3.1",
        "matplotlib >= 3.2.0"
    ],
    python_requires='>=3.6',
)

from setuptools import setup

with open("README.rst", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="ChemPlot", 
    version="",
    author="Murat Cihan Sorkun",
    author_email="m.c.sorkun@differ.nl",
    description="A python library for chemical space visualization.",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/mcsorkun/ChemPlot",
    license="BSD",
    packages=["chemplot"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
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
    ]
    python_requires='>=3',
)

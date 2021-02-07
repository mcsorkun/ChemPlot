from setuptools import setup, find_packages

setup(
    name="ChemPlot", 
    version="",
    author="Murat Cihan Sorkun",
    author_email="m.c.sorkun@differ.nl",
    description="A python library for chemical space visualization.",
    long_description=long_description,
    long_description_content_type="",
    url="https://github.com/mcsorkun/ChemPlot",
    license="BSD 3-Clause License"
    packages=find_packages(exclude=['docs']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
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

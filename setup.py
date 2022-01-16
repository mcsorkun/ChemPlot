from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="chemplot", 
    version="1.2.0",
    author="Murat Cihan Sorkun, Dajt Mullaj",
    author_email="mcsorkun@gmail.com, dajt.mullai@gmail.com",
    description="A python library for chemical space visualization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mcsorkun/ChemPlot",
    project_urls={
        "Bug Tracker": "https://github.com/mcsorkun/ChemPlot/issues",
	"Documentation": "https://chemplot.readthedocs.io/en/latest/"
    },
    license="BSD",
    packages=["chemplot", "chemplot.tests"],
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
    keywords="chemoinformatics, dimension reduction",
    install_requires=[
	"pandas>=1.1.3",
	"numpy>=1.19.2",
	"matplotlib>=3.3.2",
	"seaborn>=0.11.1",
	"umap-learn>=0.5.1",
	"scikit-learn>=0.23.2",
	"bokeh>=2.2.3",
	"scipy>=1.5.2",
	"mordred>=1.2.0",
    "networkx>=2.5"
    ],
    test_suite="pytest",
    tests_require=[
    "pytest>=6.2.4",
    ],
    include_package_data=True,
    package_data={'': ['data/*.csv'], 'chemplot.tests': ['test_data/*.csv']},
    python_requires='>=3.6',
)

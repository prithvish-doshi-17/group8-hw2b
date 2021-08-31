
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HW2B",  # Replace with your own username
    version="0.0.1",
    author="Vraj Chokshi",
    author_email="vschoksh@ncsu.edu",
    description="This is a just a simple setup file",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prithvish-doshi-17/group8-hw2b.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
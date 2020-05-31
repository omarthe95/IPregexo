import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="IPregexo", 
    version="0.0.1",
    author="Omar Adil",
    author_email="xomaradilxa@gmail.com",
    description="Validating and classifying IPv4 address",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omarthe95/IPregexo",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

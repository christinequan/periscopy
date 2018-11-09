import setuptools

INSTALL_REQUIRES = [
    'numpy>=1.9.3',
    'pandas>=0.15.2',
    'matplotlib>=1.4.3',
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="periscopy",
    version="0.0.1",
    author="Christine Quan",
    author_email="christine.quan11@gmail.com",
    description="periscopy: business data visualization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    install_requires=INSTALL_REQUIRES,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
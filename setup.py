from setuptools import find_packages, setup

with open("README.md", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="the_number",
    version="0.1.0",
    author="sus2790",
    author_email="ddoaoing@gmail.com",
    description="A pure Python library for numeric type checking and validation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sus2790/the-number",
    packages=find_packages("the_number"),
    package_dir={"": "the_number"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)

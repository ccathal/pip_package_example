import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pip_package_example_cathal",
    version="0.0.2",
    author="Cathal Corbett",
    author_email="cathalcorbett3@gmail.com",
    description="Example Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ccathal/pip_package_example",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",

    ],
    license="MIT",
    python_requires='>=3.6',
)

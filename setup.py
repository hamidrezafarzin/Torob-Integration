import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "torob-integration",
    version = "0.0.1",
    author = "Hamidreza Farzin",
    author_email = "hamidfarzin1382@gmail.com",
    description = "A Python module facilitating effortless interaction with the Torob API for seamless access to product data.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/hamidrezafarzin/Torob-Integration",
    project_urls = {
        "Author": "https://github.com/hamidrezafarzin",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires = [
        'requests',
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.6"
)
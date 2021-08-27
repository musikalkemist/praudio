import setuptools
from importlib.machinery import SourceFileLoader


version = SourceFileLoader("praudio.version",
                           "praudio/version.py").load_module()

with open("requirements.txt", "r") as fp:
    required = fp.read().splitlines()

with open("README.md", "r", encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name="praudio",
    version=version.__version__,
    author="Valerio Velardo",
    author_email="velardovalerio@gmail.com",
    description="Complex preprocessing of entire audio datasets with 1 command",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/musikalkemist/praudio",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    project_urls={
        "Source": "https://github.com/musikalkemist/praudio",
        "Tracker": "https://github.com/musikalkemist/praudio/issues",
    },
    python_requires=">=3.7",
    install_requires=required,
    extras_require={
        "testing": [
            "pytest",
            "coverage",
            "pytest-mock",
            "pylint",
            "mypy"
        ]
    },
    entry_points={
        "console_scripts": [
            "preprocess = praudio.preprocess:preprocess",
        ]
    }
)
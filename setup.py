"""Setup config for Now CLI."""
import pathlib

from setuptools import setup

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")

with open("requirements.txt", "r") as requirements_file:
    requirements = [line.replace("\n", "") for line in requirements_file.readlines()]

with open("version.txt", "r") as version_file:
    version = version_file.read().strip()

setup(
    name="now-info-cli",
    version=version,
    description="Command line utilities for information about now",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-strawberry66/now-cli",
    py_modules=["now"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "now = now:cli",
        ],
    },
)

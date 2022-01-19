"""Setup config for Now CLI."""

from setuptools import setup

with open("requirements.txt", "r") as file:
    requirements = [line.replace("\n", "") for line in file.readlines()]

setup(
    py_modules=["now"],
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "now = now:cli",
        ],
    },
)

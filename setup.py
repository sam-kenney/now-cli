"""Setup config for Now CLI."""

from setuptools import setup

with open("requirements.txt", "r") as file:
    requirements = [line.replace("\n", "") for line in file.readlines()]

setup(
    py_modules=["now"],
    install_requires=requirements
    + [
        "enforce_typing @ "
        + "git+https://github.com/mr-strawberry66/python-type-enforcement"
    ],
    entry_points={
        "console_scripts": [
            "now = now:cli",
        ],
    },
)

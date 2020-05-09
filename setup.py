from setuptools import find_packages, setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name="prime_number",
    version="1.1",
    author="Nour Etienne",
    author_email="nouretienne1@gmail.com",
    description="function that establishes the prime divisors or a given number",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/nouretienne/repo-U3S1D1",
    packages=find_packages()
)
from setuptools import setup, find_packages

# Read requirements from requirements.txt
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="QASystem",
    version="0.1",
    author="Rohit",
    author_email="rohitgupta5533@gmail.com",
    packages=find_packages(),
    install_requires=requirements,
    # Add any additional setup options here
)


from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name = 'ERDot',
    version = '2.1.5',
    author="Darcy Lugt-Falk",
    author_email="darcy@darcylf.me",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ehne/ERDot",
    packages = ['erdot'],
    install_requires=[
        'Click',
    ],
    entry_points = {
        'console_scripts': [
            '''erdot = erdot.__main__:main'''
        ],
    },
    python_requires='>=3',
    )

# notes so that d remembers how to do pypi
# 1. make sure you've got the env open
# 2. run python3 setup.py bdist_wheel
# 3a. to test, run pip install . 
# 3b. to publish, run twine upload --skip-existing dist/*

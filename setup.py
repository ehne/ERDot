from setuptools import setup
with open("README.md", "r") as fh:
    long_description = fh.read()
setup(
    name = 'ERDot',
    version = '0.1.2',
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
from setuptools import setup

setup(
    name = 'ERDot',
    version = '0.1.0',
    packages = ['erdot'],
    install_requires=[
        'Click',
    ],
    entry_points = {
        'console_scripts': [
            '''erdot = erdot.__main__:main'''
        ]
    })
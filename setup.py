from setuptools import setup

setup(
    name='Handle',
    version='0.0.1',
    packages=[
        'handle'
    ],
    install_requires=[
        'click==6.6',
    ],
    entry_points={
        'console_scripts': [
            'handle = cli:cli'
        ]
    }
)

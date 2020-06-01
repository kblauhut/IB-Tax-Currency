from setuptools import setup

setup(
    name='ibtc',
    version='1.0',
    description='Uses Interactive Brokers report csv files to calculate profit in a specified currency.',
    author='Kolja Blauhut',
    packages=['ibtc'],
    entry_points={
        'console_scripts': ['run=ibtc.core:main'],
    },
    install_requires=['requests']
)

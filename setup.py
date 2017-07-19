from setuptools import setup

setup(
    name='notes',
    packages=['notes'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pymongo'
    ],
)

from setuptools import setup

setup(
    name='melete-core',
    version='0.0.1',
    install_requires=['mecab-python', 'mido'],
    packages=['melete'],
    package_data={'melete': ['melete/dicrc']}
)

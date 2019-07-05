from setuptools import find_packages, setup

setup(
    name='pyvww',
    packages=find_packages(),
    version='0.1.0',
    description='Python API to work with the Visual Wake Words Dataset.',
    author='Maxim Bonnaerens',
    license='',
    install_requires=[
        'pycocotools'
        ]
)

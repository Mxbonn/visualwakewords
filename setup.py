import os
import io
from setuptools import find_packages, setup


def read(*names, **kwargs):
    with io.open(os.path.join(os.path.dirname(__file__), *names),
                 encoding=kwargs.get("encoding", "utf8")) as fp:
        return fp.read()


readme = read('README.md')

setup(
    name='pyvww',
    packages=find_packages(),
    version='0.1.1',
    description='Python API to work with the Visual Wake Words Dataset.',
    long_description=readme,
    long_description_content_type="text/markdown",
    author='Maxim Bonnaerens',
    author_email="maxim@bonnaerens.be",
    url='https://github.com/Mxbonn/visualwakewords',
    license='Apache 2.0',
    install_requires=[
        'pycocotools',
        'torchvision'
        ]
)

import sys

try:
    from setuptools import setup
except ImportError:
    # Use distutils.core as a fallback.
    # We won't be able to build the Wheel file on Windows.
    from distutils.core import setup

if sys.version_info < (3, 5, 0):
    raise RuntimeError('`hearken` requires Python 3.5.0+')

version = '0.1.0'

requires = ['requests']

setup(
    name='hearken',
    version=version,
    author='PeterDing',
    author_email='dfhasyt@gmail.com',
    license='MIT',
    description='a Tool for language learner',
    url='http://github.com/PeterDing/hearken',
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
    packages=['hearken'],
    scripts=['bin/hearken'],
    include_package_data=True
)

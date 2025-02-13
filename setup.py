from setuptools import find_packages, setup

from tastytrade import VERSION


f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='tastytrade',
    version=VERSION,
    description='An unofficial API for Tastytrade!',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Graeme Holliday',
    author_email='graeme.holliday@pm.me',
    url='https://github.com/tastyware/tastytrade',
    license='Apache',
    install_requires=[
        'aiohttp<4',
        'requests<3',
        'tastyworks-aiocometd>=1.0',
        'dataclasses'
    ],
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    include_package_data=True,
)

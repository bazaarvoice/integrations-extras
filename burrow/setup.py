from codecs import open  # To use a consistent encoding
from os import path

from setuptools import setup

HERE = path.dirname(path.abspath(__file__))

# Get version info
ABOUT = {}
with open(path.join(HERE, 'datadog_checks', 'burrow', '__about__.py')) as f:
    exec(f.read(), ABOUT)

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


CHECKS_BASE_REQ = 'datadog-checks-base==6.0.1'


setup(
    name='datadog-burrow',
    version=ABOUT['__version__'],
    description='The burrow check',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='datadog agent burrow check',
    # The project's main homepage.
    url='https://github.com/DataDog/integrations-extras',
    # Author details
    author='David J. Garcia',
    author_email='david.garcia@bazaarvoice.com',
    # License
    license='BSD-3-Clause',
    # See https://pypi.org/classifiers
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: System :: Monitoring',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.7',
    ],
    # The package we're going to ship
    packages=['datadog_checks.burrow'],
    # Run-time dependencies
    install_requires=[CHECKS_BASE_REQ],
    # Extra files to ship with the wheel package
    include_package_data=True,
)

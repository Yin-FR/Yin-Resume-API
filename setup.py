import sys
from setuptools import setup, find_packages

NAME = "yin_resume_api"
VERSION = "1.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
    "connexion>=2.0.2",
    "swagger-ui-bundle>=0.0.2",
    "python_dateutil>=2.6.0"
]

setup(
    name=NAME,
    version=VERSION,
    description="Yin Resume API",
    author_email="",
    url="",
    keywords=["OpenAPI", "Yin Resume API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['openapi/openapi.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['yin_resume_api=yin_resume_api.__main__:main']},
    long_description="""\
    This is Flask API server of https://Yin-FR.github.io, generated by OpenAPI.
    """
)


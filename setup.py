import os

from setuptools import find_packages, setup

# single source of truth for package version
version_ns = {}
with open(os.path.join("globus_search_cli", "version.py")) as f:
    exec(f.read(), version_ns)


setup(
    name="globus-search-cli",
    version=version_ns["__version__"],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "globus-sdk>=1.7.0,<2.0.0",
        "click>=6.7,<7.0",
        "configobj>=5.0.6,<6.0.0",
    ],
    entry_points={"console_scripts": [("globus-search = globus_search_cli:cli_root")]},
    description="Globus Search CLI",
    long_description=open("README.rst").read(),
    author="Stephen Rosen",
    author_email="sirosen@globus.org",
    url="https://github.com/globus/globus-search-cli",
    keywords=["globus", "cli", "command line", "search"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
)

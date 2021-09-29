import os

from setuptools import find_packages, setup

MYPY = False
if MYPY:
    from tryping import Any, Dict

# single source of truth for package version
version_ns = {}  # type: Dict[Any, Any]
with open(os.path.join("globus_search_cli", "version.py")) as f:
    exec(f.read(), version_ns)


setup(
    name="globus-search-cli",
    version=version_ns["__version__"],
    include_package_data=True,
    packages=find_packages(),
    install_requires=[
        "click>=8.0,<9.0",
        "globus-sdk>=3.0.2,<4",
        "globus-sdk-tokenstorage==0.4.1",
    ],
    extras_require={
        "dev": [
            # testing
            "pytest<5.0",
            "pytest-cov<3.0",
            # mocking HTTP responses
            "responses==0.14.0",
            # reading fixture data from config
            "pyyaml",
        ]
    },
    entry_points={"console_scripts": [("globus-search = globus_search_cli:cli_root")]},
    description="Globus Search CLI",
    long_description=open("README.rst").read(),
    author="Stephen Rosen",
    author_email="sirosen@globus.org",
    url="https://github.com/globus/globus-search-cli",
    keywords=["globus", "cli", "command line", "search"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)

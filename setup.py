import os
from setuptools import setup, find_packages

# single source of truth for package version
version_ns = {}
with open(os.path.join("globus_search_cli", "version.py")) as f:
    exec(f.read(), version_ns)


setup(name='globus-search-cli', version=version_ns["__version__"],
      description='Globus Search CLI',
      include_package_data=True, packages=find_packages(),

      install_requires=[
        'globus-sdk>=1.5.0,<2.0.0',
        'click>=6.7,<7.0',
        'configobj>=5.0.6,<6.0.0',
      ],

      entry_points={
          'console_scripts': [
              ('globus-search = globus_search_cli:cli_root')
          ]
      })

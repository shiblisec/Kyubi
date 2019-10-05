from setuptools import setup

setup(name='kyubi',
      version='0.1.0',
      packages=['kyubi'],
      install_requires=['colorterm', 'requests', 'colorama', 'pyfiglet', 'argparse'],
      entry_points={
          'console_scripts': [
              'kyubi = kyubi.core:main'
          ]
      },
      )

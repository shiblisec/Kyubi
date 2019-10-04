from setuptools import setup

setup(name='kyubi',
      version='0.1.0',
      packages=['kyubi'],
      entry_points={
          'console_scripts': [
              'kyubi = kyubi.core:main'
          ]
      },
      )

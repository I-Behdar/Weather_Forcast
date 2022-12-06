from distutils.core import setup

setup(name='weather_app',
      version='1.0',
      description='Weather forcast',
      packages=['weather_app'],
      install_requires=[
        "pandas",
      ]
     )
from setuptools import setup

setup(name="LEDtester",
      version="0.2",
      description="LED Testing for COMP30670 Assignment 3",
      url="",
      author="Michael Herron",
      author_email="michael.herron@ucdconnect.ie",
      licence="GPL3",
      packages=['Assignment3'],
      entry_points={
          'console_scripts':['Assignment3_led_tester=Assignment3.main_lights:main']
          },
      install_requires=[
          'numpy',
          'argparse',
          ]
      )
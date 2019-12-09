# pythonic-garage-band

**Author**: Ting Luo
**Version**: 1.0.0

## Overview
An application that creates bands, musicians(who can plays instruments) by utilizing the classes feature in Python.

## Getting Started
The user is required to first navigating to the folder contatining the source codes. The user can then enter the virtual environment (by typing "pipenv shell") and run the source codes (by typing "python3 band.py") and test suites (by typing "pytest") in Python3.

## Architecture
The pytest framewrok is installed for testing purpose. pytest library is imported to test_band.py .

## API
The Band class has attributes name and members, as well as a method get_members_names that returns members' names, a play_solo method that asks each member musician to play a solo, a class method to_list which returns a list of previously created Band instances, and a static method create_from_data which takes a collection of formatted data and returns a created Band instance.

The Musician class has attributes name, instrument and solo. A get_instrument method that returns a string of an instrument, and a play_solo method that returns string of an instrument solo.

## Change Log
12-06-2019 8:00 AM - Added functions.
12-08-2019 4:30 PM - Added create_from_data function & tested.

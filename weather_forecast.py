import pandas as pd # Library for data manipulation -> turns weather data into clean table (DataFrame)
import numpy as np # Math Library for calculations
from weather_day import WeatherDay

"""
This files takes the raw JSON data from the API and cleans it up for display

Dependent on weather_day.py
"""

def __init__(self,raw_data):
  self.raw_data=raw_data
  self.days=self.create_days()
  self.dataframe=self.create_dataframe()

def create_days(self):

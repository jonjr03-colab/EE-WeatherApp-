import pandas as pd # Library for data manipulation -> turns weather data into clean table (DataFrame)
import numpy as np # Math Library for calculations
from weather_day import WeatherDay

class WeatherForecast: 
  """
  Represents a 7-day forecast
  This files takes the raw JSON data from the API and cleans it up for display
  
  Dependent on weather_day.py
  """
  
  def __init__(self,raw_data):
    """
    Constructor
    Initializes the WeatherForecast object and automatically parses the data.

    Args:
        raw_data (dict): The raw JSON dictionary returned by the NWS API.
    """
    self.raw_data=raw_data
    self.days=self.create_days()
    self.dataframe=self.create_dataframe()
  
  def create_days(self):
    """
    Parses the raw JSON API data to extract daily and nightly weather metrics.
    Combines them into custom WeatherDay objects.

    Returns:
        list: A list containing exactly 7 WeatherDay objects.
    """
    days=[]
    periods=self.raw_data["properties"]["periods"]
    # NWS API provides forecast data in half-days (Day=FirstHalf Night=SecondHalf)
    for i in range(0,14,2): # By steping by 2 the loop can grab both day (i) and night (i+1)
      day=periods[i]
      night=periods[i+1]

      date=day["startTime"][:10] #grabs timestamp string from day block slicing off anything after the first 10 characters
      high=day["temperature"]
      low=night["temperature"]
      conditions=day["shortForecast"] #pulls text description of the weather (i.e., "Partly Cloudy")
      rain=day.get("probabilityOfPrecipitation",{}).get("value",0)
      rain=rain if rain is not None else 0 #Safety Check to avoid KeyError returning null for rain

      days.append(WeatherDay(date,high,low,conditions,rain))
    return days

  def create_dataframe(self):
    
    

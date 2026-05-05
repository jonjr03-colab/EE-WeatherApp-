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
    """
    Converts the list of WeatherDay objects into a pandas DataFrame.

    Returns:
      pd.DataFrame: A clean, tabular dataset containing the week's forecast
    """
    return pd.DataFrame([ # Creates the pandas DataFrame (table) and opens a dictionary
      {
        "Day":d.day_name,
        "Date":d.date,
        "High":d.high_temp,
        "Low":d.low_temp,
        "Avg":d.avg_temp,
        "Condition":d.condition,
        "Rain %":d.rain_chance
      }
      for d in self.days # tells python to build the dictionary row previously defined for every object (d) inside the self.days list
    ])

  def average_high_temp(self):
    """
    Calculates the average high temperature across the entire 7-day forecast.

    Returns:
      float: The mathematical mean of the week's high temperature.
    """
    return np.mean([d.high_temp for d in self.days]) # Grabs just the high_temp from every day in the list then np.mean() calculates the average
    

  def rainy_days(self): 
    """
    Filters the forecast to isolate days where rain is expected.

    Returns:
      list: A list of WeatherDay objects that have a rain chance greater than 0.
    """
    return list(filter(lambda d: d.is_rainy(), self.days)) # Filters every day, keeping only 
    
  def __len__(self):
    """
    The number of days currently stored in the forecast.

    Returns:
      int: The total count of WeatherDay objects in the forecast list.
    """
    return len(self.days)

  def __str__(self):
    """
    Provides a human-readable string representation of the object.

    Returns:
      str: A summary string detailing the number of days in the forecast.
    """
    return f"WeatherForcast with {len(self.days)} days"

from datetime import datetime 
"Import the 'datetime' module" 


class WeatherDay:
    """
    Represents the weather information for a specific day.

    Parameters include:
    - date (str)
    - high_temp (int)
    - low_temp (int)
    - condition (str)
    - rain_chance (int)
    """

    def __init__(self, date, high_temp, low_temp, condition, rain_chance):
        "Assigns values to the instance variables"
        self.date = date "Stores date as a string"
        self.high_temp = high_temp "Stores high temperature"
        self.low_temp = low_temp "Stores low temperature"
        self.condition = condition "Stores weather condition"
        self.rain_chance = rain_chance "Stores chances of rain"

        self.day_name = datetime.strptime(date, "%Y-%m-%d").strftime("%A") "Converts date from string format to a date object, then to day of week"
    "Calculates average temperature of the day"
    def average_temp(self):
        return (self.high_temp + self.low_temp) / 2
    "Check if the day is rainy"
    def is_rainy(self):
        return self.rain_chance > 40
    "Provids a string representation of the WeatherDay object"
    def __str__(self):
        return f"{self.day_name} ({self.date}): {self.condition}, High {self.high_temp}, Low {self.low_temp}, Rain {self.rain_chance}%"
    "Method to check if two WeatherDay objects represent same day"
    def __eq__(self, other):
        return self.date == other.date
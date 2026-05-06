from weather_day import WeatherDay # import WeatherDay class from weather_day.py
from weather_utils import classify_weather # import classify_weather function from weather_utils.py

# test temperature average calculation
def test_temp_avg():
    d = WeatherDay("2026-05-05", 65, 43, "Sunny", 10) # create a WeatherDay object

    assert d.average_temp() == 54  # check if d.average_temp() returns the correct value

# test if rainy weather is detected
def test_weather_rain():
    d = WeatherDay("2026-05-05", 70, 40, "Rain", 80) # create WeatherDay object with rain

    assert d.is_rainy() # check if d.is_rainy() returns True

# test classify_weather function
def test_weather_classify():
    d = WeatherDay("2026-05-05", 110, 70, "Hot", 10) # create WeatherDay object classified as hot

    assert classify_weather(d) == "hot" # check if it's properly classified as hot


# test the eq operator overload
def test_weather_eq(): 
    d1 = WeatherDay("2026-05-05", 70, 40, "Rain", 80) # create first object
    d2 = WeatherDay("2026-05-05", 80, 60, "Sunny", 5) # create second object

    assert d1 == d2 # check that objects are equal because the dates match

# testing
if __name__ == "__main__":

    # run all tests manually
    test_temp_avg()
    test_weather_rain()
    test_weather_classify()
    test_weather_eq()

    print("All tests passed")
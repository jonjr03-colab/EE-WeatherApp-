import matplotlib.pyplot as plt
#Import matplotlib library for plotting graphs

def plot_7_day_weather(forecast):
    """
    Plots temperatures

    Parameters: 
    - forecast: An object containing a 7-day data
    """

    df = forecast.dataframe #Gets Dataframe and attributes that contain weather data

    plt.figure() #Creates a new figure for plotting
    plt.plot(df["Day"], df["High"], marker="o", label="High") #Plots high temperatures
    plt.plot(df["Day"], df["Low"], marker="o", label="Low") #Plots low temperatures
    plt.xlabel("Day") #Labels x-axis as 'Day'
    plt.ylabel("Temperature (F)") #Labels y-axis as 'Temperature (F)'
    plt.title("7-Day Forecast") 
    plt.legend() 
    plt.show()


def classify_weather(day): 
    """
    Classifies weather

    Parameters:
    - day: A WeatherDay object holding the weather data for one day

    Returns:
    - A string classification of the weather 
    """
    # Classifies weather based on rain chance and average temperature
    if day.rain_chance > 60:
        return "rain likely"
    elif day.average_temp() > 80:
        return "hot"
    elif day.average_temp() > 60:
        return "mild"
    else:
        return "cold"
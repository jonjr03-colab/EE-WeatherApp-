import requests # third-party library for making HTTP network calls to APIs
               # requires request library in enviroment -> pip install request
"""
This file serves as the API which fetches the weather data (7 days) 
from the National Weather Service (NWS), as a JSON file,
and integrates it into our weather app.

NWS requires the coordinates to provide a specific localized URL for the region.
The NWS API is strict, requiring a form of identification (headers) in order to accept the request.
"""

# Need the localized url before the 7 day forcast can be extracted
def get_localized_forcast_url(latitude, longitude):
  """
  Retrieves localized forcast URL from NWS API.

  Parameters:
  latitude (float)
  longitude (float)

  Returns:
  Localized Forecast URL (str)
  """
  url=f"https://api.weather.gov/points/{latitude},{longitude}"

  # This is required in case the app/code spams NWS and they need a form of contact
  # Functions basically like the header of an envelope
  headers={"User-Agent":"weather-app (drubioci@stevens.edu) (msuh@stevens.edu) (jlayme@stevens.edu)"}

  try:
    response=requests.get(url, headers=headers) # gets network request
    response.raise_for_status() # Safety Check to avoid a crash from anything other than a successful 200 level code
    data=response.json() # Converts raw JavaScript Object Notation (JSON) into a searchable python dictionary
    return data["properties"]["forecast"] #Nested dictionary look-up

  #Taking into account any errors that arrise
  except requests.exceptions.RequestException as e:
    print("Error getting forcast URL:", e)
    return None

def get_7day_forecast(latitude, longitude):
  """
  Retrieves 7-day forcast data

  Dependent on get_localized_forcast_url()
  
  Parameters:
  latitude (float)
  longitude (float)

  Returns:
  Forcast JSON (dict)
  """

  # Helper Function Call
  forecast_url=get_localized_forcast_url(latitude, longitude)

  if forcast_url is None: # Fail-fast Check, if the first function failed (i.e., bad coordinates, network error)
    return None           # Avoids a crash

  headers={"User-Agent":"weather-app (drubioci@stevens.edu) (msuh@stevens.edu) (jlayme@stevens.edu)"}

  try:
    response=requests.get(forecast_url, headers=headers)
    reponse.raise_for_status()
    return response.json() 

  except requests.exceptions.RequestException as e:
    print("Error getting forcast data:", e)
    return None


# ==Test==
if __name__=="__main__":
  data=get_7day_forcast(40.74400786550859, -74.02491546017065) # Coordinates for Stevens Instutute of Technology
  print("Data fetched:", data is not None) # Prints a boolean that checks if the code is functioning

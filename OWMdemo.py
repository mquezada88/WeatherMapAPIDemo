import pyowm

owm = pyowm.OWM('your-API-key')

# Pyowm is the python OWM API wrapper that allows an easier to read interface for open weather. 

place = raw_input('Enter the city,country you wish to find information about: ')
observation = owm.weather_at_place(place)
w = observation.get_weather()
menu = {}
menu['1']="Will it be Sunny out tomorrow?" 
menu['2']="Current weather"
menu['3']="Details: Wind, Humidity, etc."
menu['4']="Exit"
while True: 
    options=menu.keys()
    options.sort()
    for entry in options: 
        print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
        # Will it be sunny tomorrow at this time?
        forecast = owm.daily_forecast(place)
        tomorrow = pyowm.timeutils.tomorrow()
        b =forecast.will_be_sunny_at(tomorrow)
        print(b)		
    elif selection == '2': 
        # Search for current weather
        observation = owm.weather_at_place(place)
        w = observation.get_weather()
        print(w)                      # <Weather - reference time
                                      # status=Clouds>
    elif selection == '3':
        # Weather details
        print(w.get_wind())                  # Example: {'speed', 'deg'}
        print(w.get_humidity())
        print(w.get_temperature())  # Example: {'temp_max','temp','temp_min'} 
    elif selection == '4': 
        break
    else: 
        print "Not a good choice!" 

# Search current weather observations in the surroundings via lat and long 
# lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)
from spread_diff import DiffSpread, WEATHER_RE, FOOTBALL_RE

"""
Basic tests without using any external testing lib
"""

weather = DiffSpread(WEATHER_RE, 'weather.dat').spread(min) == '14'
football = DiffSpread(FOOTBALL_RE, 'football.dat').spread(min) == 'Aston_Villa'
print "Weather Spread working: " + str(weather)
print "Football Spread working: " + str(football)


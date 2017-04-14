#!/usr/bin/env python2

import re

FOOTBALL_RE = re.compile(r'\s+'  # whitespaces
                         r'\d+\. '  # digit with dot (row number)
                         r'(?P<team>\w+)'  # team word
                         r'.*?'  # anything between
                         r'(?P<for>\d+)\s+-\s+(?P<ag>\d+)')  # F - A

WEATHER_RE = re.compile(r'^\s+'  # whitespaces
                        r'(?P<day>\d+)'  # day digit
                        r'\s+'
                        r'(?P<max>\d+)'  # second column (MxT)
                        r'\s+'
                        r'(?P<min>\d+)')  # third column (MnT)


class DiffSpread(object):
    """
    Class computing spread using file and regexp to parse data from file.
    Values extracted with regexp must be in this order: name, *values (2).
    Method spread(func) outputs name of min/max (func) row in file.
    """
    def __init__(self, regexp, file_name):
        self.regexp = regexp
        self.file_name = file_name

    def spread(self, func):
        res = {}
        for line in open(self.file_name):
            m = self.regexp.match(line)
            if m:
                res[m.group(1)] = abs(int(m.group(2)) - int(m.group(3)))
        return func(res, key=res.get)

if __name__ == "__main__":
    print("Day with smallest temperature spread: " +
          DiffSpread(WEATHER_RE, 'weather.dat').spread(min))
    print("Team with smallest difference in for and against goals: " +
          DiffSpread(FOOTBALL_RE, 'football.dat').spread(min))

# tests in tests.py

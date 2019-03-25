# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 17:09:13 2019
@author: h5435
"""
import datetime

print(datetime.datetime(2016, 1, 22, 14, 31, 5, 757391))

start_time = datetime.datetime.now()
print(type(start_time))

start_time = start_time.replace(year = 2017, month = 2, day = 14)
print(start_time)

how_long = datetime.datetime.now() - start_time
print(type(how_long))

print(how_long.days)
print(how_long.seconds)

hundred_after = datetime.datetime.now().replace(hour = 9, minute=0, second=0) + datetime.timedelta(days=100)
print("{}/{}/{}  {}:{}:{}".format(hundred_after.year,hundred_after.month, hundred_after.day, hundred_after.hour, hundred_after.minute, hundred_after.second))
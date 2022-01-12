# pyCal
A simple library to manage schedules in Python. I haven't been able to find any good library to manage schedules in Python for managing running tasks on multiple time slots in a day across multiple days of the week. This library aims to provide a simple way to manage this. The lack of timezone usage is intentional. The library assumes all schedules are inserted with the same timezone and all times that are checked for being in schedule follow the same timezone as the schedules. This way the schedule can remain timezone agnostic. 


# Useage:

#### _class_ **Schedule**
&emsp;The base class of pyCal. This will store the scheduling timeline for the week.

#### _method_ Schedule.**add_schedule**(start_time, end_time, days = [0, 1, 2, 3, 4, 5, 6])
&emsp;Add a schedule to the Schedule class.

&emsp;_start_time_ [`datetime.time`] (required) The start time of the schedule for the specified days. 

&emsp;_end_time_ [`datetime.time`] (required) The end time of the schedule for the specified days.

&emsp;_days_ [`list[int]`] (optional) The days of the week to apply this schedule to, with reference to the `start_time`. If the `end_time` < `start_time` then the schedule will roll over into the next day. If no value is provided, the schedule will apply to all days. 0 = Monday, 6 = Sunday.

#### _method_ Schedule.**get_schedule**() -> dict[int, list]
&emsp;Get the timeline of all currently added schedules in the `Schedule` object.

&emsp; _Returns_ [`dict[int,list]`] a dictionary with key `int` weekday and value `list` of `tuple` (start_time: datetime.time, end_time: datetime.time). 0 = Monday, 6 = Sunday. 

#### _method_ Schedule.**clear_schedule**(days = [0, 1, 2, 3, 4, 5, 6])
&emsp;Clear the schedules of the specified days from the `Schedule` object.

&emsp;_days_ [`list[int]`] (optional) The days of the week to clear the schedule of. If no day is provided, it will clear the schedule of all days. 

#### _method_ Schedule.**in_schedule**(time) -> bool:
&emsp;Check if the specified time is within schedule. 

&emsp;_time_ [`datetime.datetime`] (optional) A datetime value to check. If no value is provided, it will check if the current system time is within schedule. 

&emsp; _Returns_ [`bool`] Boolean `True` = the time is within schedule. `False` = The time is outside schedule. 


# Example

```
from pycal import Schedule
from datetime import datetime, time

sched = Schedule()
sched.add_schedule(time(10,0,0), time(18,0,0), days=[0,1,2,3,4])
print(sched.in_schedule(datetime(2022, 1, 12, 12, 0, 0)))
```

Output:
```
True
```
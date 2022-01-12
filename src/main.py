import datetime
import time
from typing import Union, List, Optional, Dict
from collections import defaultdict


class Schedule:
    def __init__(self):
        self.schedule: Dict[int, list] = defaultdict(list)

    def add_schedule(
        self,
        start_time: datetime.time,
        end_time: datetime.time,
        days: List[int] = [0, 1, 2, 3, 4, 5, 6],
    ):
        """Add a schedule to the Schedule object.

        Args:
            start_time [datetime.time] : The start time of the schedule.
            end_time [datetime.time]: The end time of the schedule. If end_time < start_time, the schedule will roll over to the next day.
            days [list[int]]: The days of the week that the schedule applies to, with reference to start_time. 0 = Monday, 6 = Sunday. If no value is provided, schedule will apply to all days.
        """
        for day in days:
            if end_time > start_time:
                self.schedule[day].append((start_time, end_time))
            else:
                self.schedule[day].append((start_time, self.dt_ceil(start_time)))
                self.schedule[(day + 1) % 7].append((self.dt_floor(end_time), end_time))

    def get_schedule(self):
        """Returns the schedule as a dictionary.

        Returns:
            dict: A dictionary of schedules.
        """
        return self.schedule

    def clear_schedule(self, days: List[int] = [0, 1, 2, 3, 4, 5, 6]):
        """Clear the schedule for the specified days.

        Args:
            days (List[int], optional): Days to clear schedule from. Defaults to [0,1,2,3,4,5,6]. 0 = Monday, 6 = Sunday.
        """
        for day in days:
            self.schedule[day] = []

    def in_schedule(self, time: Optional[datetime.datetime]) -> bool:
        """Check if the time is in the schedule.

        Args:
            time (datetime.time, optional): Time to check. Defaults to None.

        Returns:
            bool: True if time is in schedule, False if not.
        """
        if time is None:
            time = datetime.datetime.now()
        day = time.weekday()
        if day in self.schedule:
            for start, end in self.schedule[day]:
                if start <= time.time() < end:
                    return True
        return False

    @staticmethod
    def dt_ceil(dt: datetime.time, scale: str = "day"):
        if scale == "day":
            return datetime.time(23, 59, 59, 999999)
        elif scale == "hour":
            return datetime.time(dt.hour, 59, 59, 999999)
        elif scale == "minute":
            return datetime.time(dt.hour, dt.minute, 59, 999999)
        elif scale == "second":
            return datetime.time(dt.hour, dt.minute, dt.second, 999999)
        else:
            raise ValueError(
                "Invalid scale. Scale must be one of [day, hour, minute, second]"
            )

    @staticmethod
    def dt_floor(dt: datetime.time, scale: str = "day"):
        if scale == "day":
            return datetime.time(0, 0, 0, 0)
        elif scale == "hour":
            return datetime.time(dt.hour, 0, 0, 0)
        elif scale == "minute":
            return datetime.time(dt.hour, dt.minute, 0, 0)
        elif scale == "second":
            return datetime.time(dt.hour, dt.minute, dt.second, 0)
        else:
            raise ValueError(
                "Invalid scale. Scale must be one of [day, hour, minute, second]"
            )


def main():
    pass


if __name__ == "__main__":
    main()

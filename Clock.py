class clockTime:
    def __init__(self):
        self.hours = 0
        self.mins = 0
        self.secs = 0

    def set_hours(self, hours):
        self.hours = hours

    def set_mins(self, mins):
        self.mins = mins

    def set_secs(self, secs):
        self.secs = secs

    def set_time(self, hours, mins, secs):
        self.hours = hours
        self.mins = mins
        self.secs = secs

    def show_time(self):
        print(f"{self.hours}:{self.mins}:{self.secs}")


clock = clockTime()
print("Set the time now.")
hours = input("hours: ")
min = input("min: ")
secs = input("secs: ")
clock.set_time(hours, min, secs)
clock.show_time()


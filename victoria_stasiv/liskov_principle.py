class Worker(object):
    def __init__(self, position):
        self.position = position
    def dayshift_hours(self, hours):
        self.position[1] += hours
    def nightshift_hours(self, hours):
        self.position[0] += hours
class RetiredMan(object):
        WORKING_HOURS  = (0)

        def __init__(self):
            self.position = type(self).WORKING_HOURS
def main():
    retired_man = RetiredMan()

    print("The retiredman going to work for 10 hours in dayshift and 3 hours at the nightshift")
    try:
        retired_man.dayshift_hours(10)
        retired_man.nightshift_hours(-3)
    except:
        pass
    print("The hours worked by retiredman {}".format(retired_man.WORKING_HOURS))
    print("The current position of the retiredman {}". format(retired_man.position))
if __name__ == "__main__":
    main()

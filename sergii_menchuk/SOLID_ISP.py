from abc import ABCMeta, abstractmethod
import time


class TimeStamp(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def time_stamp(self):
        pass


class EnterTime(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def enter_time(self):
        pass


class ExitTime(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def exit_time(self):
        pass


class Logger(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def logger(self):
        pass


class EnterOffice(TimeStamp, EnterTime, Logger):
    def time_stamp(self):
        return time.time()

    def enter_time(self):
        return time.time()

    def logger(self):
        print('Employee entered office at {}'.format(self.time_stamp()))


class ExitOffice(TimeStamp, ExitTime, Logger):
    def time_stamp(self):
        return time.time()

    def exit_time(self):
        return time.time()

    def logger(self):
        print('Employee exited office at {}'.format(self.time_stamp()))


class ChangeFloor(TimeStamp, Logger):
    def time_stamp(self):
        return time.time()

    def logger(self):
        print('Employee changed office floor at {}'.format(self.time_stamp()))


def main():
    enter_office = EnterOffice()
    exit_office = ExitOffice()
    change_floor = ChangeFloor()

    enter_office.logger()
    time_start = enter_office.enter_time()
    time.sleep(4)
    change_floor.logger()
    time.sleep(2)
    change_floor.logger()
    time.sleep(1)
    exit_office.logger()
    time_stop = exit_office.exit_time()
    print("Employee spent {} at the office". format(time_stop - time_start))


if __name__ == '__main__':
    main()


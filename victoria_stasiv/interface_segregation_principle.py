from abc import ABCMeta, abstractmethod
class Workable(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def work(self):
        pass
class Eatable(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def eat(self):
        pass
class AbstractWorker(Workable, Eatable):
    pass
class Worker(AbstractWorker):
    def work(self):
        print("I am working")
    def eat(self):
        print("I am eating")
class NewWorker(AbstractWorker):
    def work(self):
        print("I work very hard")
    def eat(self):
        print("I am eating fast")

class Manager(object):
    def __init__(self):
        self.worker = None
class WorkManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Workable), "'worker must be of type{}".format(Workable)
        self.worker = worker
    def manage(self):
        self.worker.work()
class BreakManager(Manager):
    def set_worker(self, worker):
        assert isinstance(worker, Eatable), "'worker' must be of type{}".format(Eatable)
        self.worker = worker
    def lunch_break(self):
        self.worker.eat()
class Clock(Workable):
    def work(self):
        print("I am a clock. I am working")
def main():
    work_manager = WorkManager()
    break_manager = BreakManager()
    work_manager.set_worker(Worker())
    break_manager.set_worker(Worker())
    work_manager.manage()
    break_manager.lunch_break()
    work_manager.set_worker(Clock())
    work_manager.manage()
    try:
        break_manager.set_worker(Clock())
        break_manager.lunch_break()
    except:
        pass
if __name__ == '__main__':
    main()

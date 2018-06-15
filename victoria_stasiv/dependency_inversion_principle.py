from abc import ABCMeta, abstractmethod
class ITeacher(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def work(self):
        pass
class Teacher(ITeacher):
    def work(self):
        print("I am teaching")
class HeadTeacher(object):
    def __init__(self):
        self.teacher = None
    def set_worker(self, teacher):
        assert isinstance(teacher, ITeacher), "'worker' must be of type{}".format(Teacher)
        self.teacher = teacher
    def manage(self):
        if self.teacher is not None:
            self.teacher.work()
class PhysicsTeacher(ITeacher):
    def work(self):
        print("I teach  Physics")
class SportsTeacher(ITeacher):
    def work(self):
        print("I teach Sports")
def main():
    teacher = Teacher()
    headteacher =  HeadTeacher()
    headteacher.set_worker(teacher)
    headteacher.manage()
if __name__ == "__main__":
    main()

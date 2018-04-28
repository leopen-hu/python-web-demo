class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        if self.score >= 80:
            return 'B'
        elif self.score >= 60:
            return 'C'
        else:
            return 'D'


studentA = Student('Brain', 89)
studentB = Student('gallory', 67)
studentA.print_score()
studentB.print_score()
print(studentA.get_grade())
print(studentB.get_grade())


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return str(self._width) + '*' + str(self._height)


s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == '1024*768':
    print('测试通过!')
else:
    print('测试失败!')

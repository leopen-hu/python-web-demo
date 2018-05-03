class Query(object):
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...', self.name)


with Query('dd') as q:
    q.query()


# contextlib
print('contextlib------------------------------------')

from contextlib import contextmanager  # nopep8


class Query(object):
    def __init__(self, name):
        self.name = name

    def query(self):
        print('Query info about %s...', self.name)


@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')


with create_query('df') as d:
    d.query()

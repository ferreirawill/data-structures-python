import abc


class Deque(metaclass=abc.ABCMeta):
    '''Deque is a generalization of FIFO Queue and LIFO Queue'''

    def add_first(self, value):
        raise NotImplementedError

    def remove_first(self):
        raise NotImplementedError

    def add_last(self, value):
        raise NotImplementedError

    def remove_last(self):
        raise NotImplementedError

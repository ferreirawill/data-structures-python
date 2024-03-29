import abc


class Deque(metaclass=abc.ABCMeta):
    '''Deque is a generalization of FIFO Queue and LIFO Queue'''

    @abc.abstractmethod
    def add_first(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_first(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_last(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def remove_last(self):
        raise NotImplementedError

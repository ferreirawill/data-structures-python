import abc


class Stack(metaclass=abc.ABCMeta):
    '''Stacks are Queue LIFO'''

    @abc.abstractmethod
    def push(self, label):
        '''Add element to the last position'''
        raise NotImplementedError

    @abc.abstractmethod
    def pop(self):
        '''Remove element to the last position'''
        raise NotImplementedError

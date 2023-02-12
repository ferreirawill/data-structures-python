import abc


class Stack(metaclass=abc.ABCMeta):
    '''Stacks are Queue LIFO'''

    def push(self, label):
        '''Add element to the last position'''
        raise NotImplementedError

    def pop(self):
        '''Remove element to the last position'''
        raise NotImplementedError

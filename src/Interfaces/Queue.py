import abc


class Queue(metaclass=abc.ABCMeta):
    '''Queue FIFO'''

    @abc.abstractmethod
    def add(self, label):
        '''Add element to the first position'''
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self):
        '''Remove element to the last position'''
        raise NotImplementedError

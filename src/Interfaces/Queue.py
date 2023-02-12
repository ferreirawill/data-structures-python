import abc


class Queue(metaclass=abc.ABCMeta):
    '''Queue FIFO'''

    def add(self, label):
        '''Add element to the first position'''
        raise NotImplementedError

    def remove(self):
        '''Remove element to the last position'''
        raise NotImplementedError

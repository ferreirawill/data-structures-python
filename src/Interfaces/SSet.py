import abc


class SSet(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def size(self):
        raise NotImplementedError

    @abc.abstractmethod
    def find(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self, value):
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self, value):
        raise NotImplementedError

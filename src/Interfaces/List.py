import abc


class List(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def size(self):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self,position):
        raise NotImplementedError

    @abc.abstractmethod
    def set(self,position,value):
        raise NotImplementedError

    @abc.abstractmethod
    def add(self,position,value):
        raise NotImplementedError

    @abc.abstractmethod
    def remove(self,position):
        raise NotImplementedError

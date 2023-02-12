from src.ArrayLists.ArrayStack import ArrayStack
from src.Interfaces.List import List


class DualArrayDeque(List):
    def __init__(self):
        self.front = ArrayStack()
        self.back = ArrayStack()
    def size(self):
        return self.front.size() + self.back.size()

    def get(self, position):
        if position < self.front.size():
            return self.front.get(self.front.size()-position-1)
        else:
            return self.back.get(position-self.front.size())

    def set(self, position, value):

        if position < self.front.size():
            return self.front.set(self.front.size()-position-1,value)
        else:
            return self.back.set(position-self.front.size(), value)

    def add(self, position, value):
        if position < self.front.size():
            self.front.add(self.front.size()-position,value)
        else:
            self.back.add(position-self.front.size(),value)

        self.__balance()

    def remove(self, position):
        if position < self.front.size():
            removed_value = self.front.remove(self.front.size()-position-1)
        else:
            removed_value = self.back.remove(position- self.front.size())

        self.__balance()
        return removed_value

    def __balance(self):
        length = self.size()
        mid = length//2

        if 3*self.front.size() < self.back.size() or 3*self.back.size() <self.front.size():
            new_ars_front = ArrayStack()
            new_ars_back = ArrayStack()

            for idx in range(mid):
                new_ars_front.add(idx,self.get(mid-idx-1))

            for idx in range(length-mid):
                new_ars_back.add(idx, self.get(mid + idx))

            self.front = new_ars_front
            self.back = new_ars_back






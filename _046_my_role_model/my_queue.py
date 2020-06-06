
class Queue:
    def __init__(self, capacity):
        self.__back = 0
        self.__front = 0
        self.list = [0] * capacity

    @property
    def size(self):
        if self.__back - self.__front >= 0:
            return self.__back - self.__front
        return self.__front + len(self.list) - self.__back

    def increase_back(self):
        self.__back += 1
        if self.__back >= len(self.list):
            self.__back = self.__back - len(self.list)

    def increase_front(self):
        self.__front += 1
        if self.__front >= len(self.list):
            self.__front = self.__front - len(self.list)

    def push_back(self, x):
        if self.size < len(self.list):
            self.list[self.__back] = x
            self.increase_back()
            return True
        return False

    def front(self):
        if self.size > 0:
            return self.list[self.__front]
        return None

    def pop_front(self):
        if self.size > 0:
            ans = self.list[self.__front]
            self.increase_front()
            return ans
        return None

    def get_element(self, x):
        if x >= len(self.list):
            return None
        if x + self.__front - 1 < len(self.list):
            return self.list[x + self.__front - 1]
        return self.list[x + self.__front - 1 - len(self.list)]

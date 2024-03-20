class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return f"{self.size * '🍪'}"

    def deposit(self, n):
        if n > self.capacity:
            raise ValueError
        if self.size + n > self.capacity:
            raise ValueError
        self._size += n

    def withdraw(self, n):
        if self.size < n:
            raise ValueError
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @size.setter
    def size(self, size):
        self._size = size

#def main():
#    jar = Jar()
#    jar.deposit(6)
#    jar.withdraw(3)
#    print(jar)
#
#if __name__ == "__main__":
#    main()

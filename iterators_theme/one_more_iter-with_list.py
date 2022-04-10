class TestIter:
    def __init__(self) -> None:
        self.test_data = [1, 2, 3]

    def __iter__(self):
        self.iter_length = len(self.test_data)
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.iter_length:
            val = self.test_data[self.i]
            self.i += 1
            return val
        raise StopIteration

for i in TestIter():
    print(i)

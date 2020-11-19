class NegativeSumError(Exception):
    def __init__(self):
        self.error = 'Sum cannot be negative!!!'
        super().__init__(self.error)


def sum_with_exceptions(a, b):
    if a + b >= 0:
        return a + b
    else:
        raise NegativeSumError


if __name__ == '__main__':
    sum_with_exceptions(4, -5)

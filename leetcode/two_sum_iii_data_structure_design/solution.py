from collections import defaultdict


class TwoSum:

    def __init__(self):
        self.numbers = defaultdict(int)

    def add(self, number):
        self.numbers[number] += 1

    def find(self, value):
        for num in self.numbers:
            complement = value - num
            if complement == num:
                if self.numbers[num] > 1:
                    return True
            else:
                if complement in self.numbers:
                    return True
        return False

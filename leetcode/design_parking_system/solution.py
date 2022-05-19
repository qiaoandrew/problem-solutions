class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.max_big = big
        self.max_medium = medium
        self.max_small = medium
        self.cur_big = self.cur_medium = self.cur_small = 0

    def addCar(self, carType: int) -> bool:
        if carType == 0:
            if self.cur_big < self.max_big:
                self.cur_big += 1
                return True
            else:
                return False
        elif carType == 1:
            if self.cur_medium < self.max_medium:
                self.cur_medium += 1
                return True
            else:
                return False
        else:
            if self.cur_small < self.max_small:
                self.cur_small += 1
                return True
            else:
                return False

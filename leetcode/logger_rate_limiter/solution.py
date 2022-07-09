class Logger:

    def __init__(self):
        self.next_print = {}

    def should_print_message(self, timestamp, message):
        if message in self.next_print:
            if timestamp < self.next_print[message]:
                return False
            else:
                self.next_print[message] = timestamp + 10
                return True
        else:
            self.next_print[message] = timestamp + 10
            return True

from collections import defaultdict


class ValidWordAbbr:

    def __init__(self, dictionary):
        self.abbreviations = defaultdict(set)
        for word in dictionary:
            abbreviation = word
            if len(word) > 2:
                abbreviation = word[0] + str(len(word) - 2) + word[-1]
            self.abbreviations[abbreviation].add(word)

    def is_unique(self, word):
        abbreviation = word
        if len(word) > 2:
            abbreviation = word[0] + str(len(word) - 2) + word[-1]
        return abbreviation not in self.abbreviations or (
            len(self.abbreviations[abbreviation]) == 1
            and word == list(self.abbreviations[abbreviation])[0])

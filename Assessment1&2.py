class Letter:
    def __init__(self, words):
        self.word = words.lower()
        self.alphabets = 'abcdefghijklmnopqrstuvwxyz'

    def calc_pos(self):
        positions = [self.alphabets.index(c) + 1 for c in self.word]
        return positions

    def result(self):
        positions = self.calc_pos()
        result_word = self.word.upper()
        result_positions = ','.join(map(str, positions))

        print("Result =", result_word)
        print("Result =", result_positions)


class SumValues(Letter):
    def __init__(self, wrd):
        super().__init__(wrd)

    # Assessment 2
    def numValues(self):
        positions = self.calc_pos()
        total = sum(positions) + 1
        print(f"Letter Values :", positions)
        print("Added one total is :", total)


if __name__ == "__main__":
    word: str = "light"

    print("Assessment 1:")
    word_convert = Letter(word)
    word_convert.result()

    print("Assessment 2:")
    sum_calc = SumValues(word)
    sum_calc.numValues()

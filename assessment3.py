class Words:
    def __init__(self, word1, word2, word3):
        self.word1 = word1
        self.word2 = word2
        self.word3 = word3

    def result1(self):
        result = self.word1 + " " + self.word2
        print("Result 1:", result)

    def result2(self):
        result = "[" + self.word1 + "]" + "[" + self.word2 + "]"
        print("Result 2:", result)

    def result3(self):
        result = self.word1 + " " + self.word2 + " " + self.word3[0]
        print("Result 3:", result)

if __name__ == "__main__":
    word1 = "MY"
    word2 = "PURPOSE"
    word3 = ["IN LIFE"]

    d_results = Words(word1, word2, word3)

    print("Result 1:")
    d_results.result1()
    print()
    print("Result 2:")
    d_results.result2()
    print()
    print("Result 3 =:")
    d_results.result3()

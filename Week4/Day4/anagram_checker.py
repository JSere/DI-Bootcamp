class AnagramChecker:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.word_list = [line.strip().upper() for line in file]

    def is_valid_word(self, word):
        return word.upper() in self.word_list

    def is_anagram(self, word1, word2):
        w1 = word1.lower()
        w2 = word2.lower()
        if w1 == w2:
            return False
        return sorted(w1) == sorted(w2)

    def get_anagrams(self, word):
        anagrams = []
        for w in self.word_list:
            if self.is_anagram(word, w):
                anagrams.append(w.lower())
        return anagrams
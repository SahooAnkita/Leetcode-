class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        # Number of pattern characters and words must be same
        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}

        for char, word in zip(pattern, words):

            # char already maps to a different word
            if char in pattern_to_word and pattern_to_word[char] != word:
                return False

            # word already maps to a different character
            if word in word_to_pattern and word_to_pattern[word] != char:
                return False

            pattern_to_word[char] = word
            word_to_pattern[word] = char

        return True
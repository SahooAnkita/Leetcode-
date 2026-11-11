class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26

            # Count characters
            for ch in word:
                count[ord(ch) - ord('a')] += 1

            # Convert list to tuple so it can be used as dictionary key
            key = tuple(count)

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())
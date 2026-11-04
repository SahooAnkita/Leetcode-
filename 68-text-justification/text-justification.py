class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0

        while i < len(words):
            # Find all words that can fit in this line
            line_words = []
            line_length = 0

            while i < len(words):
                word = words[i]

                # Minimum 1 space between words
                required_length = line_length + len(word)

                if line_words:
                    required_length += 1

                if required_length > maxWidth:
                    break

                line_words.append(word)
                line_length = required_length
                i += 1

            # Check if this is the last line
            is_last_line = i == len(words)

            # Last line or line with only one word
            if is_last_line or len(line_words) == 1:
                line = " ".join(line_words)
                line += " " * (maxWidth - len(line))
                result.append(line)
                continue

            # Fully justify the line
            total_spaces = maxWidth - sum(len(word) for word in line_words)
            gaps = len(line_words) - 1

            # Minimum spaces for each gap
            spaces_per_gap = total_spaces // gaps

            # Extra spaces go to the left gaps
            extra_spaces = total_spaces % gaps

            line = ""

            for j, word in enumerate(line_words):
                line += word

                if j < gaps:
                    spaces = spaces_per_gap

                    if j < extra_spaces:
                        spaces += 1

                    line += " " * spaces

            result.append(line)

        return result
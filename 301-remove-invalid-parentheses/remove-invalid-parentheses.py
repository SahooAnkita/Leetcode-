class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        def is_valid(string):
            balance = 0

            for char in string:
                if char == '(':
                    balance += 1
                elif char == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        result = []
        queue = {s}
        found = False

        while queue:

            next_level = set()

            for current in queue:

                if is_valid(current):
                    result.append(current)
                    found = True

            # If valid strings are found at this level,
            # we don't remove any more characters.
            if found:
                return result

            for current in queue:

                for i in range(len(current)):

                    # Only remove parentheses.
                    if current[i] not in "()":
                        continue

                    # Avoid generating the same string
                    # by removing consecutive identical parentheses.
                    if i > 0 and current[i] == current[i - 1]:
                        continue

                    new_string = current[:i] + current[i + 1:]

                    next_level.add(new_string)

            queue = next_level

        return result
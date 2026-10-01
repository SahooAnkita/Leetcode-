class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        for char in s:

            # Opening bracket
            if char in '([{':
                stack.append(char)

            # Closing bracket
            else:
                # No opening bracket to match
                if not stack:
                    return False

                # Top bracket doesn't match
                if stack[-1] != pairs[char]:
                    return False

                # Matching bracket found
                stack.pop()

        # Valid only if all opening brackets were closed
        return len(stack) == 0
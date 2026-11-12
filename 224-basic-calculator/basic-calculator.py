class Solution:
    def calculate(self, s: str) -> int:
        stack = []

        result = 0
        number = 0
        sign = 1

        for char in s:

            # Build the number
            if char.isdigit():
                number = number * 10 + int(char)

            # Addition
            elif char == '+':
                result += sign * number
                number = 0
                sign = 1

            # Subtraction
            elif char == '-':
                result += sign * number
                number = 0
                sign = -1

            # Opening parenthesis
            elif char == '(':
                stack.append(result)
                stack.append(sign)

                result = 0
                sign = 1

            # Closing parenthesis
            elif char == ')':
                result += sign * number
                number = 0

                previous_sign = stack.pop()
                previous_result = stack.pop()

                result = previous_result + previous_sign * result

            # Ignore spaces

        result += sign * number

        return result
class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()

        while n != 1:

            # If we have already seen n, we are in a cycle
            if n in seen:
                return False

            seen.add(n)

            # Calculate sum of squares of digits
            total = 0

            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10

            n = total

        return True
class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        n = len(expression)

        def dfs(index):
            result = set()
            current = {""}

            while index < n and expression[index] != "}":

                # Union
                if expression[index] == ",":
                    result.update(current)
                    current = {""}
                    index += 1

                # Braced expression
                elif expression[index] == "{":
                    inside, index = dfs(index + 1)

                    # Concatenate current with inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                # Normal character
                else:
                    char = expression[index]
                    current = {word + char for word in current}
                    index += 1

            result.update(current)

            # Skip '}'
            if index < n and expression[index] == "}":
                index += 1

            return result, index

        result, _ = dfs(0)

        return sorted(result)
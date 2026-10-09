class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_count = 0

        i = 0

        while i < len(s):
            if s[i] == '(':
                open_count += 1
            else:
                # Check whether we have a pair of ')'
                if i + 1 < len(s) and s[i + 1] == ')':
                    i += 1
                else:
                    # Insert one ')' to complete the pair
                    insertions += 1

                # Match the closing pair with an opening '('
                if open_count > 0:
                    open_count -= 1
                else:
                    # Insert an opening '('
                    insertions += 1

            i += 1

        # Every remaining '(' needs two ')'
        insertions += open_count * 2

        return insertions
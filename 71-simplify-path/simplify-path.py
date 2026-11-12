class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for part in path.split('/'):
            
            # Ignore empty parts and current directory
            if part == '' or part == '.':
                continue

            # Go to parent directory
            elif part == '..':
                if stack:
                    stack.pop()

            # Valid directory/file name
            else:
                stack.append(part)

        return '/' + '/'.join(stack)
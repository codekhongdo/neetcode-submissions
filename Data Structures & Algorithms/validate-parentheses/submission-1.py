class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }

        stack = []

        for char in s:
            if char in bracket:
                stack.append(char)
            else:
                if not stack:
                    return False

                if bracket[stack.pop()] != char:
                    return False

        return len(stack) == 0
            
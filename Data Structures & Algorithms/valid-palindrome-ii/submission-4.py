class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left, right, k):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                elif k == 0:
                    # gặp mismatch lần đầu: thử cả 2 hướng, k đánh dấu đã dùng quyền xóa
                    return check(left + 1, right, 1) or check(left, right - 1, 1)
                else:
                    return False
            return True

        return check(0, len(s) - 1, 0)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for k in nums:
            if k in seen:
                return True
            seen.add(k)
        return False
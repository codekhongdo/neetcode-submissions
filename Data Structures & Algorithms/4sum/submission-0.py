class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        list_arr = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                new_target = target - nums[i] - nums[j]
                left, right = j + 1, n - 1
                while left < right:
                    s = nums[left] + nums[right]
                    if s == new_target:
                        list_arr.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1
                    elif s < new_target:
                        left += 1
                    else:
                        right -= 1
        return list_arr
        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        A=0
        right=len(numbers)-1
        left=0
        while (A==0):
            sum=numbers[right]+numbers[left]
            if(sum==target):
                return [left+1,right+1]
            elif(sum>target):
                right-=1
            else:
                left+=1
            
        

        
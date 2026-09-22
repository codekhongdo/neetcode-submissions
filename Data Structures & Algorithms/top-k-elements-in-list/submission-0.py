class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_list={}
        for i in nums:
            my_list[i]=my_list.get(i,0)+1
        top_k = heapq.nlargest(k, my_list, key=my_list.get)
        return top_k
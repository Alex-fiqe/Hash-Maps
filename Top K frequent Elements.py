class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0) + 1
        sorted_nums=sorted(fre,key=fre.get,reverse=True)  
        return sorted_nums[:k]

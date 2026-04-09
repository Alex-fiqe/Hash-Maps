class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre={}
        for i in nums:
            fre[i]=fre.get(i,0) + 1
        sorted_nums=sorted(fre,key=fre.get,reverse=True)  
        return sorted_nums[:k]
#sorted(freq)-->This means: sort the keys of the dictionary
#key=fre.get-->this means: sort in their fre not in their key
#reverse=True--> This means: reverse in decending order(the highest fre in the first)

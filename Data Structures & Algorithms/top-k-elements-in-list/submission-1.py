class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        for num in nums:
            if num not in a:
                a[num] = 1
            else:
                a[num] += 1
        sorted_dict = dict(sorted(a.items(), key=lambda item: item[1]))
        return list(sorted_dict.keys())[-k:]        
                
            
                


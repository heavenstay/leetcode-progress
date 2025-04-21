# Problem: Top K Frequent Elements: https://leetcode.com/problems/top-k-frequent-elements/
# Difficulty: Easy
# Time Taken: 20 min
# Attempts: 1
# Hints Used: No
# Notes: We use a hash_map to store the number of time an element appear in the array. Then we sort this map by the number of time they appear and return the number of elements asked by k. 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}

        for num in nums: 
            hash_map[num] = hash_map.get(num, 0) + 1

        filtered_dict = dict(sorted(hash_map.items(), key=lambda item: item[1], reverse=True))
        return list(filtered_dict)[:k]
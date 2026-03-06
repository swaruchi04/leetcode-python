from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        return [num for num, freq in count.most_common(k)]


# Example
nums = [1,1,1,2,2,3]
k = 2

sol = Solution()
print(sol.topKFrequent(nums, k))

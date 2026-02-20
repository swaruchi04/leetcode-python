from collections import Counter

def topKFrequent(nums, k):
    count = Counter(nums)
    return [num for num, freq in count.most_common(k)]


# Example test
print(topKFrequent([1,1,1,2,2,3], 2))  # Output: [1,2]

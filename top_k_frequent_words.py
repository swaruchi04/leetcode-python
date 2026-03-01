from collections import Counter

def topKFrequent(words, k):
    count = Counter(words)
    return sorted(count, key=lambda w: (-count[w], w))[:k]


print(topKFrequent(
    ["i","love","leetcode","i","love","coding"], 2
))

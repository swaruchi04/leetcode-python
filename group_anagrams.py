from collections import defaultdict

def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())


# Example test
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

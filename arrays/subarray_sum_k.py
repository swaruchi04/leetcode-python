def subarraySum(nums, k):
    count = 0
    prefix_sum = 0
    hashmap = {0: 1}

    for num in nums:
        prefix_sum += num
        count += hashmap.get(prefix_sum - k, 0)
        hashmap[prefix_sum] = hashmap.get(prefix_sum, 0) + 1

    return count


print(subarraySum([1,1,1], 2))  # Output: 2

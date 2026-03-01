def rotate(nums, k):
    k %= len(nums)

    # reverse whole array
    nums.reverse()
    # reverse first k elements
    nums[:k] = reversed(nums[:k])
    # reverse remaining elements
    nums[k:] = reversed(nums[k:])

    return nums


print(rotate([1,2,3,4,5,6,7], 3))

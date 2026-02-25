def maxProduct(nums):
    cur_max = cur_min = result = nums[0]

    for n in nums[1:]:
        temp = (cur_max * n, cur_min * n, n)
        cur_max = max(temp)
        cur_min = min(temp)
        result = max(result, cur_max)

    return result


print(maxProduct([2,3,-2,4]))  # 6

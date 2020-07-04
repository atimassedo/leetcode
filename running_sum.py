def running_sum(nums):
    i = 1
    while i < len(nums):
        nums[i] += nums[i - 1]
        i+=1

    return nums

print(running_sum([5,2,3,4]))

        


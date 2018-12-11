#%%
def first_duplicate(a):
    rmv_dup = set()
    for nums in a:
        if nums not in rmv_dup:
            rmv_dup.add(nums)
        else:
            return nums
    return -1

first_duplicate([3,4,5,1,5,1])
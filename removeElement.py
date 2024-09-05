nums = [3,2,2,3]
val = 3
start=0
for i in nums:
    if i!=val:
        nums[start]=i
        start+=1
print(start)
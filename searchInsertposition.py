nums=[1,2,3,6]
target=5
start=0
end=len(nums)-1
while start<=end:
    m=(start+end)//2
    if nums[m]==target:
        print(m)
        break
    elif nums[m]>target:
        end=m-1
    elif nums[m]<target:
        start=m+1
else:
    print(start)
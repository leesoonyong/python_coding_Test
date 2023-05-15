nums = [4,1,9,7,5,3,16]
target = 14;
answer = False;

for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        if nums[i] + nums[j] == target:
            answer = True;
print(answer)
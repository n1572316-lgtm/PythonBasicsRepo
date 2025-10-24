num: int = int(input())

nums: list[int] = []

for i in range(num):
    nums.append(int(input()))


    index: int = 0

    while index < len(nums):
        if nums[i] % 3 == 0 or nums[i] % 5 == 0:
            nums.pop(i)
        index += 1

    for num in nums:
        print(num, end="")


print(nums)

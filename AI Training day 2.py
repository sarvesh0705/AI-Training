nums = [3, 0, 1]
print(sum(range(len(nums)+1)) - sum(nums))


arr = [1, 4, 3, 2, 6, 5]
arr.reverse()
print(arr)


nums = [3, 2, 2, 3]
val = 3

nums = [x for x in nums if x != val]
print(len(nums))
print(nums)

nums = [3, 2, 2, 3]
val = 3

nums = [x for x in nums if x != val]
print(len(nums))
print(nums)


nums = [1, 1, 2, 2, 3]

nums = list(dict.fromkeys(nums))
print(len(nums))
print(nums)



nums = [0, 1, 0, 3, 12]

nums.sort(key=lambda x: x == 0)
print(nums)



arr = [100, 200, 300, 400]
k = 2

s = sum(arr[:k])
m = s

for i in range(k, len(arr)):
    s += arr[i] - arr[i-k]
    m = max(m, s)

print(m)



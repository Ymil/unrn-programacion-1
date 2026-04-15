nums = [10, -1,2,3,5,7,6,-7,8,-10]

print("De la lista son multiplos de 2 los siguientes numeros:")

for i in range(len(nums)):
    if not nums[i]%2:
        print(nums[i])

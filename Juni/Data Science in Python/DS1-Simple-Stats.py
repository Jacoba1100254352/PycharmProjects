def count(nums):
	return len(nums)


def my_sum(nums):
	total = 0
	for num in nums:
		total += num
	return total


def mean(nums):
	if len(nums) == 0:
		return None
	return my_sum(nums) / len(nums)


def median(nums):
	if len(nums) == 0:
		return None
	nums.sort()
	middle = int(len(nums) / 2)
	if len(nums) % 2 == 1:
		return nums[middle]
	else:
		return (nums[middle - 1] + nums[middle]) / 2


def my_max(nums):
	if len(nums) == 0:
		return None
	max_so_far = nums[0]
	for num in nums:
		if num > max_so_far:
			max_so_far = num
	return max_so_far


def my_min(nums):
	if len(nums) == 0:
		return None
	min_so_far = nums[0]
	for num in nums:
		if num < min_so_far:
			min_so_far = num
	return min_so_far


def my_range(nums):
	return my_max(nums) - my_min(nums)


def summary(nums):
	print('SUMMARY:')
	print(nums)
	print("Count:", count(nums))
	print("Sum:", my_sum(nums))
	print("Mean:", mean(nums))
	print("Median:", median(nums))
	print("Max:", my_max(nums))
	print("Min:", my_min(nums))
	print("Range:", my_range(nums))
	print()


data1 = [-21, -15, -60, -60, -45, -34, -20, -21, -10, -30]
data2 = [54, 54, 56, 56, 56, 51, 57, 57, 57, 58, 51, 54]
data3 = [32, 43, 87, 56, 34, 21, 21, 90, 76, 72]

summary(data1)
summary(data2)
summary(data3)

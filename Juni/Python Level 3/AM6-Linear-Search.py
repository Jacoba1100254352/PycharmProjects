def linearSearch(arr, val):
	for item in arr:
		if item == val:
			return True
	return False


nums = [1, 2, 3, 4, 5]
print(linearSearch(nums, 4))
print(linearSearch(nums, 6))

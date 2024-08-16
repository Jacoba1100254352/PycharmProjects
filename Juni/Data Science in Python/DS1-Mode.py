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
  middle = int(len(nums)/2)
  return nums[middle]

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
  return my_max(nums)-my_min(nums)

def mode(nums):
  freqencies = {}
  for num in nums:
    if num in freqencies:
      freqencies[num] += 1
    else:
      freqencies[num] = 1
  max_so_far = 0
  modes = []
  for num in freqencies:
    if freqencies[num] > max_so_far:
      modes = [num]
      max_so_far = freqencies[num]
    elif freqencies[num] == max_so_far:
      modes.append(num)
  return modes

def summary(nums):
  stats = {}
  stats["Data:"] = nums
  stats["Count:"] = count(nums)
  stats["Sum:"] = my_sum(nums)
  stats["Mean:"] = mean(nums)
  stats["Median:"] = median(nums)
  stats["Max:"] = my_max(nums)
  stats["Min:"] = my_min(nums)
  stats["Range:"] = my_range(nums)
  stats["Mode(s):"] = mode(nums)
  return stats

def print_stats(stats):
  print("SUMMARY:")
  for key in stats:
    print(key, stats[key])
  print()

data1 = [-21,-15,-60,-60,-45,-34,-20,-21,-10,-30]
data2 = [54,54,56,56,56,51,57,57,57,58,51,54]
data3 = [32,43,87,56,34,21,21,90,76,72,63]

stats1 = summary(data1)
stats2 = summary(data2)
stats3 = summary(data3)

print_stats(stats1)
print_stats(stats2)
print_stats(stats3)




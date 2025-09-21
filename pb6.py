# if lst is null or empty. -> []
# if all numbers < threshold. -> [counter]
# if all numbers > threshold. -> [0]

# function count_less_thab (numbers, threshold)
# count = 0
# for number in lst
#   if num < lst
#       count += 1
#  return count

def count_less_than(numbers, threshold):
    count = 0
    for num in numbers:
        if num < threshold:
            count += 1
    return count

numbers = [12,8,2,4,4,10]
counter = count_less_than(numbers, 5)
print(counter)
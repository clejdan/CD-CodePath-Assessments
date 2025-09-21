# Can it take in strings? No
# If list is null or empty -> []
# If multiplied by 0 -> 0

# function doubled 
#   prints out num in list multiplied by 2


def doubled(lst):
    for num in lst:
        num *= 2
        print(num)

doubled([1,2,3])
doubled ([])
doubled ([0,0,0])
doubled (["h", 2,3])
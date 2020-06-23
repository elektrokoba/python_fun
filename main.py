array = [1,2,7,3,4,5,5,6,7,8,9,9]
k = 3

def canBePartitioned(array, k):
  return arraySizeDivisableByK(array, k) and subarraysContainUniqueElems(array, len(array) / k)
  
def arraySizeDivisableByK(array, k):
  return len(array) % k == 0

def subarraysContainUniqueElems(array, maxRepetition):
  array.sort()
  counter = 1
  for i in range(1, len(array)):
    if array[i] == array[i - 1]:
      counter += 1
      if counter > maxRepetition:
        return False
    else:
      counter = 1
  return True
  
print(canBePartitioned(array, k))
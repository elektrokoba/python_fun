def separateEvenOdd(numbers):
  left=0
  right=len(numbers) - 1

  while left < right:
    while left < right and isEven(numbers[left]):
        left += 1
    while left < right and isOdd(numbers[right]):
        right -= 1
    swap(numbers, left, right)
  return numbers

def isEven(num):
  return num %2 == 0

def isOdd(num):
  return not isEven(num)

def swap(numbers,i,j):
  temp = numbers[i]
  numbers[i] = numbers[j]
  numbers[j] = temp

#numbers = [12,9,8,2,6,7,2,3,4,5]
#[12,4,8,2,6,7,2,3,9,5]
#[12,4,8,2,6,2,7,3,9,5]
numbers = [1,2,3,4,6,5,7,8,9,10]

print(separateEvenOdd(numbers))

# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). 
# Find two lines, which together with x-axis forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

# The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.

# Example:
# input = [1,8,6,2,5,4,8,3,7]
# Output: 49

def getMaxArea(input):
    maxArea = 0

    for i in range(0, len(input)):
        for j in range((i + 1) , len(input)):
            currentArea = searchMin(input[i], input[j]) * (j - i)
            if currentArea > maxArea:
                    maxArea = currentArea
    return maxArea


def searchMin(h1, h2):
    if h1 > h2:
        return h2
    else:
        return h1

print('Largest area is: ', getMaxArea([1,8,6,2,5,4,8,3,7]))
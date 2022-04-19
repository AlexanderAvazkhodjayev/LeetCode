# Given an array of integers nums, return the number of good pairs.

# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

# Example 1:
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.

# Example 2:
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.

# Example 3:
# Input: nums = [1,2,3]
# Output: 0
 
# Constraints:
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100

def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 0
        goodPairCounter = 0
        print("array: " + str(nums))
        for x in range(0,len(nums)):
            currentItem = nums[x]
            print("Current Element: " + str(currentItem))
            for y in range(counter+1, len(nums)):
                if currentItem == nums[y]:
                    print("Match: " + str((currentItem, nums[y])))
                    goodPairCounter += 1
                else:
                    continue
            counter+=1
        print(goodPairCounter)
        return(goodPairCounter)
    
#numIdenticalPairs([1,2,3,1,1,3])


# Best Solution
def betterNumIdenticalPairs(nums):

    counter = 0
    dic = {}

    for i in nums:
        if i in dic:
            counter += dic[i]
            dic[i] += 1
        else:
            dic[i] = 1
    print(counter)
    return counter
        
betterNumIdenticalPairs([1,2,3,1,1,3,1])
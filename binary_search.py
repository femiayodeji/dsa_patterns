class BinarySearch:
    def brute(nums = [-1, 0, 3, 5, 9, 12],  target = 9):
        for k,v in enumerate(nums):
            if v == target:
                return k
        return -1

    def optimal(nums = [-1, 0, 3, 5, 9, 12],  target = 9):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right)//2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
            
        return -1

class MatrixSearch:
    def solve(matrix = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ],
    target = 3):
        
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == target:
                    return True

        return False

    def optimal(matrix = [
        [1,  3,  5,  7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ],
    target = 3):
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * rows - 1
        
        while (left <= right):
            mid = (left + right)//2
            row = mid//cols
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif target > value:
                left = mid + 1
            else:
                right = mid - 1
            
        
        return False

class EatPileInTime:
    def brute(piles = [3, 6, 7, 11],  h = 8):
        k = 1
        
        while(True):
            hour = 0
            for pile in piles:
                hour += pile/k
            if hour <= h:
                return k
            k += 1

    def optimal(piles = [3, 6, 7, 11],  h = 8):
        from functools import reduce
        
        left = 1
        right = max(piles)
        result = right
        while(left <= right):
            k = (left+right)//2
            
            hour = reduce(lambda x, y: x + y, piles) / k
            
            if hour <= h:
                result = k
                right = k - 1
            elif hour > h:
                left = k + 1
            else:
                right = k - 1

        return result

class RotatedSortedArray:
    def brute(nums = [4, 5, 6, 7, 0, 1, 2]):
        pivot = nums[0]
        for num in nums:
            if num < pivot:
                pivot = num
        return pivot

    def solve(nums = [4, 5, 6, 7, 0, 1, 2]):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)//2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        return nums[left]
            
class SearchRotatedSortedArray:
    def brute(nums = [4, 5, 6, 7, 0, 1, 2],  target = 0):
        for k,v in enumerate(nums):
            if nums[k] == target:
                return k
        return -1

    def optimal(nums = [4, 5, 6, 7, 0, 1, 2], target = 0):
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[right] > nums[mid]:
                if target >= nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        
        return -1

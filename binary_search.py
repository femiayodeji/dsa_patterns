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
        import math
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        left = 0
        right = rows * rows - 1
        
        while (left <= right):
            mid = (left + right)//2
            row = math.floor(mid/cols)
            col = mid % cols
            value = matrix[row][col]
            
            if value == target:
                return True
            elif target > value:
                left = mid + 1
            else:
                right = mid - 1
            
        
        return False

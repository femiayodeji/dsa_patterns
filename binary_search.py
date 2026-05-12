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

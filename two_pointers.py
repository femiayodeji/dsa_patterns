class Palidrome:
    def brute(str = "A man, a plan, a canal: Panama"):
        cleaned = "".join(char.lower() for char in str if char.isalnum())
        return cleaned == cleaned[::-1]

    def optimal(str = "A man, a plan, a canal: Panama"):
        left = 0
        right = len(str) - 1
        while (left < right):
            if not str[left].isalnum():
                left += 1
            elif not str[right].isalnum():
                right -= 1
            elif str[left].lower() != str[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True

class TwoSum:
    def brute(nums = [2, 7, 11, 15], target = 9):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i+1, j+1]

    def optimal(nums = [2, 7, 11, 15], target = 9):
        left = 0
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right]
            if sum == target:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            elif sum > target:
                right -= 1

class ThreeSum:
    def brute(nums = [-1, 0, 1, 2, -1, -1, -1 -4]):
        result = {}
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    sum = nums[i] + nums[j] + nums[k]
                    if sum == 0:
                        values = [nums[i], nums[j], nums[k]]
                        key = f"{nums[i]}_{nums[j]}_{nums[k]}"
                        result[key] = values
        
        return list(result.values())

    def optimal(nums = [-1, 0, 1, 2, -1, -1, -1 -4]):
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -1 * nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]: left += 1
                    while left < right and nums[right] == nums[right - 1]: right -= 1
                    left += 1
                    right -= 1
                elif sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
        return result

class WaterContainer:
    def brute(heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]):
        max_water = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                height = heights[i] if heights[i] < heights[j] else heights[j]
                width = j - i
                water = width * height
                max_water = max_water if max_water > water else water
        return max_water
    

    def optimal(heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]):
        max_water = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            width = right - left
            height = heights[left] if heights[left] < heights[right] else heights[right]
            water = width * height
            max_water = max(max_water, water)
            if heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        return max_water

class RainWater:
    def brute(heights = [0, 1, 0, 2, 1, 0, 1, 3, 1, 0, 1, 2]):
        total_water = 0
        for i in range(len(heights)):
            max_left = max(heights[:i+1])
            max_right = max(heights[i:])
            water = min(max_left, max_right) - heights[i]
            total_water += water
        
        return total_water

    def optimal(heights = [0, 1, 0, 2, 1, 0, 1, 3, 1, 0, 1, 2]):
        total_water = 0
        left = 0
        max_left = 0
        right = len(heights)-1
        max_right = 0
        
        while left < right:
            if heights[left] <= heights[right]:
                if max_left <= heights[left]:
                    max_left = heights[left]
                else:
                    total_water += max_left - heights[left]
                left += 1
            else:
                if max_right <= heights[right]:
                    max_right = heights[right]
                else:
                    total_water += max_right - heights[right]
                right -= 1
        return total_water


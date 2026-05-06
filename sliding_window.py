class BestBuy:
    def brute(prices = [7, 1, 5, 3, 6, 4]):
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(profit, max_profit)
        return max_profit

    def optimal(prices = [7, 1, 5, 3, 6, 4]):
        max_profit = 0
        min_price = float('inf')
        for right in range(len(prices)):
            if prices[right] < min_price:
                min_price = prices[right]
            else:
                max_profit = max(prices[right]-min_price, max_profit)
        return max_profit

class LongestSubstringWithNoRepetition:
    def brute(str = "abcabcbb"):
        result = ""
        for i in range(len(str)):
            for j in range(i, len(str)):
                sub = str[i:j+1]
                if len(set(sub)) == len(sub) and len(sub) > len(result):
                    result = sub
        return result
        
    def optimal(str = "pwwkew"):
        result = ""
        seen = set()
        left = 0
        for right in range(len(str)):
            while str[right] in seen:
                if len(result) < len(str[left:right]):
                    result = str[left:right]
                seen.remove(str[left])
                left += 1
            seen.add(str[right])
        return result
    
class MininumWindowSubstring:
    def brute(s = "ADOBECODEBANC",  t = "ABC"):
        min_len = float('inf')
        start = end = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                needed_characters_map = {}
                for c in t:
                    needed_characters_map[c] = needed_characters_map.get(c, 0) + 1
                for c in sub:
                    if c in needed_characters_map:
                        needed_characters_map[c] -= 1
                contained = list(filter(lambda x: needed_characters_map[x] > 0, needed_characters_map))
                if len(contained) == 0:
                    if j - i + 1 < min_len:
                        min_len = j - i +1
                        start = i
                        end = j
        return s[start:end+1] if min_len != float('inf') else ""

    def optimal(s = "ADOBECODEBANC",  t = "ABC"):
        needed_characters_map = {}
        for c in t:
            needed_characters_map[c] = needed_characters_map.get(c, 0) + 1
        required_characters_n = len(needed_characters_map.keys())
        substring_characters_map = {}
        formed = 0

        min_len = float('inf')
        start = end = 0
        left = 0
        
        for right in range(len(s)):
            char = s[right]
            substring_characters_map[char] = substring_characters_map.get(char, 0) + 1
            if char in needed_characters_map and needed_characters_map[char] == substring_characters_map[char]:
                formed += 1

            while formed == required_characters_n:
                if right - left + 1 < min_len:
                    start = left
                    end = right
                    min_len = right - left + 1
                    
                left_char = s[left]
                substring_characters_map[left_char] -= 1
                if left_char in needed_characters_map and substring_characters_map[left_char] < needed_characters_map[left_char]:
                    formed -= 1
                left += 1
        return s[start:end+1] if min_len != float('inf') else ""

class SlidingWindowMaximum:
    def brute_raw(nums = [1, 3, -1, -3, 5, 3, 6, 7],  k = 3):
        result = []
        start = 0
        for i in range(k-1, len(nums)):
            result.append(max(nums[start:i+1]))
            start += 1
        return result

    def brute(nums = [1, 3, -1, -3, 5, 3, 6, 7],  k = 3):
        result = []
        start = 0
        for i in range(len(nums)-k+1):
            m = float('-inf')
            for j in range(i, i+k):
                m = max(m, nums[j])
            result.append(m)
        return result

    def optimal_raw(nums = [1, 3, -1, -3, 5, 3, 6, 7],  k = 3):
        result = []
        deque = []
        for right in range(len(nums)):
            num = nums[right]
            while len(deque) > 0 and deque[-1] < num:
                deque.pop()
            deque.append(right)
            
            if deque[0] < right - k + 1:
                deque.pop(0)
                
            if right + 1 >= k:
                result.append(nums[deque[0]])

        return result

    def optimal(nums = [1, 3, -1, -3, 5, 3, 6, 7],  k = 3):
        from collections import deque
        result = []
        q = deque() 
        
        for right in range(len(nums)):
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)
            
            if q[0] < right - k + 1:
                q.popleft()
                
            if right + 1 >= k:
                result.append(nums[q[0]])

        return result

class LongestRepeatingCharacterReplacememt:
    def brute(s = "AABABBA",  k = 1):
        max_len = 0        
        for i in range(len(s)):
            count = {}
            max_freq = 0
            for j in range(i, len(s)):
                sub = s[i:j+1]
                char = s[j]
                count[char] = count.get(char, 0) + 1
                
                max_freq = max(count[char], max_freq)
                
                window_size = j - i + 1
                required_replacement = window_size - max_freq
                
                if required_replacement <= k:
                    max_len = max(window_size, max_len)
        return max_len


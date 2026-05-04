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
        result = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                sub = s[i:j+1]
                t_count = {}
                for c in t:
                    t_count[c] = t_count.get(c, 0) + 1
                for c in sub:
                    if c in t_count:
                        t_count[c] -= 1
                contained = list(filter(lambda x: t_count[x] > 0, t_count))
                if len(contained) == 0:
                    if len(result) == 0:
                        result = sub
                    elif len(sub) < len(result):
                        result = sub
        return result


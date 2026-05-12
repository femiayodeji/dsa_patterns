class ProductArrayExceptSelfNoDivision:
    def brute(nums = [1, 2, 3, 4]):
        products = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j]
            products.append(product)
        return products
        
    def optimal(nums = [1, 2, 3, 4]):
        products = []
        prefix = 1
        for i in range(len(nums)):
            products.append(prefix)
            prefix *= nums[i]

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] *= suffix
            suffix *= nums[i]

        return products

class TwoSum:
    def solve(nums = [2, 7, 11, 15], target = 9):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def optimal(nums = [2, 7, 11, 15], target = 9):
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [seen[diff], i]
            seen[nums[i]] = i 
        return []

class ContainDuplicate:
    def brute(nums = [1, 2, 3, 1]):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

    def optimal(nums = [1, 2, 3, 1]):
        seen = set()
        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
        return False

    def optimal_raw(nums = [1, 2, 3, 1]):
        return len(set(nums)) != len(nums)

class GroupAnagram:
    def brute(words = ["eat", "tea", "tan", "ate", "nat", "bat"]):
        result = []
        used = [False] * len(words)
        
        for i in range(len(words)):
            word = words[i]
            x = "".join(sorted(list(word)))
            if used[i]:
                continue
            
            group = [word]
            for j in range(i+1, len(words)):
                y = "".join(sorted(list(words[j])))
                if not used[j] and (x == y):
                    group.append(words[j])
                    used[j] = True
            result.append(group)
        return result

    def optimal(words = ["eat", "tea", "tan", "ate", "nat", "bat"]):
        groups = {}
        for word in words:
            sorted_word = "".join(sorted(list(word)))
            if sorted_word not in groups:
                groups[sorted_word] = [word]
            else:
                groups[sorted_word].append(word)
            
        return list(groups.values())

class TopKFrequent:
    def brute(nums = [1, 1, 1, 2, 2, 3],  k = 2):
        result = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        counts = dict(sorted(counts.items(), key=lambda x: x[1], reverse=True))
        
        for count in counts:
            result.append(count)
            k -= 1
            if k <=0:
                break
            
        return result

    def optimal(nums = [1,1,1,2,2,3],  k = 2):
        result = []
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in counts.items():
            bucket[freq].append(num) 
        
        for i in range(len(bucket)-1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return []


    def optimal_raw(nums = [1,1,1,2,2,3],  k = 2):
        import heapq
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        min_heap = []
        for num, freq in counts.items():
            heapq.heappush(min_heap, (freq, num))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return [item[1] for item in min_heap]

    
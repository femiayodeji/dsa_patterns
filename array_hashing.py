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

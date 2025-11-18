class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        maximum = nums[0]
        minimum = 0
        curr = 0
        currMin = 0
        for i in range(len(nums)):
            minimum = i if nums[i] < nums[minimum] else minimum
            curr += nums[i]
            print(curr)
            if curr < 0:
                curr = 0
            else:
                if maximum < curr:
                    maximum = curr
        curr = 0
        for i in nums[minimum+1:] + nums[:minimum]:
            curr += i
            if curr < 0:
                curr = 0
            else:
                maximum = max(maximum, curr)
        return maximum
s = Solution()
print(s.maxSubarraySumCircular([5,-3,5]))
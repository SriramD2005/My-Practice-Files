def minimumPairRemoval(nums) -> int:
        res=0
        while True:
            print(nums)
            if all(nums[i]<nums[i+1] for i in range(len(nums)-1)):
                 print("hell9o")
                 break
            minsum=float('inf')
            minindex=0
            for i in range(len(nums)-1):
                sum=nums[i]+nums[i+1]
                minsum=sum if sum<minsum else minsum
                minindex=i
            nums[minindex]=minsum
            nums.pop(minindex+1)
            res+=1
            
        return res
print(minimumPairRemoval([5,2,3,1]))
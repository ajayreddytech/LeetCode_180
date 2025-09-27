class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # initially answer array stores only ones
        # then we store prefix products in it
        # then we multiply with suffix products to get final answer array
        answer = [1]*n 

        # to compute prefix products
        #runningProduct accumulates all, as it goes through the loop, but here, it is a step back
        runningProduct = 1 
        for i in range(len(nums)):
            if i==0:
                continue
            answer[i] = runningProduct * nums[i-1]
            runningProduct *= nums[i-1] 

        # to multiply answer array with suffix products
        # looping from the back
        # runningProduct accumulates all, as it goes through the loop, 
        # but here, since loop is from back, it accumulates from back 
        runningProduct = 1
        for i in range(len(nums)-1, -1, -1):
            answer[i] *= runningProduct
            runningProduct *= nums[i]
        
        return answer
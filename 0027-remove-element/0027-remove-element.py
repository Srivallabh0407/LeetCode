class Solution:
    
    def removeElement(self, nums: List[int], val: int) -> int:
        if val in nums :    
            
            nums.remove(val)
            self.removeElement(nums,val)
        
        
        

        
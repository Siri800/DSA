class Solution:
    def uniformArray(self,nums1:List[int])->bool:
        smallest_number=min(nums1)
        if smallest_number%2==1:
            return True
        for number in nums1:
            if number%2==1:
                return False
        return True
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        great_element={}
        for num in reversed(nums2):
            while stack and stack[-1]<=num:
                stack.pop()
            if stack:
                great_element[num]=stack[-1]
            else:
                great_element[num]=-1
            stack.append(num)
        return[great_element[num] for num in nums1]

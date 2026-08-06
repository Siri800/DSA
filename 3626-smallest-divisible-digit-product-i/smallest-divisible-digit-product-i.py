class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            number=n
            digit_product=1
            while number>0:
                digit=number%10
                digit_product*=digit
                number//=10
            if digit_product%t==0:
                return n
            n+=1
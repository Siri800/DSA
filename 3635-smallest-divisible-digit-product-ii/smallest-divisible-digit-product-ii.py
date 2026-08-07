class Solution:
    def smallestNumber(self,num:str,t:int)->str:
        factors=[0,0,0,0]
        primes=[2,3,5,7]
        for i in range(4):
            while t%primes[i]==0:
                factors[i]+=1
                t//=primes[i]
        if t!=1:
            return "-1"
        target2,target3,target5,target7=factors
        digit_factors={2:(1,0),3:(0,1),4:(2,0),6:(1,1),8:(3,0),9:(0,2)}
        dp=[[100]*(target3+1) for _ in range(target2+1)]
        dp[0][0]=0
        for count2 in range(target2+1):
            for count3 in range(target3+1):
                if count2==0 and count3==0:
                    continue
                for digit in digit_factors:
                    add2,add3=digit_factors[digit]
                    new2=max(0,count2-add2)
                    new3=max(0,count3-add3)
                    dp[count2][count3]=min(dp[count2][count3],dp[new2][new3]+1)
        def minimum_digits(count2,count3,count5,count7):
            return dp[count2][count3]+count5+count7
        prefix2=[0]*(len(num)+1)
        prefix3=[0]*(len(num)+1)
        prefix5=[0]*(len(num)+1)
        prefix7=[0]*(len(num)+1)
        first_zero=len(num)
        for i, character in enumerate(num):
            digit=int(character)
            add2, add3=digit_factors.get(digit,(0,0))
            prefix2[i+1]=min(target2,prefix2[i]+add2)
            prefix3[i+1]=min(target3,prefix3[i]+add3)
            prefix5[i+1]=min(target5,prefix5[i]+(digit==5))
            prefix7[i+1]=min(target7,prefix7[i]+(digit==7))
            if digit==0 and first_zero==len(num):
                first_zero=i
        if first_zero==len(num) and prefix2[-1]>=target2 and prefix3[-1]>=target3 and prefix5[-1]>=target5 and prefix7[-1]>=target7:
            return num
        def get_remaining(count2,count3,count5,count7,digit):
            add2,add3=digit_factors.get(digit,(0,0))
            return (max(0,target2-count2-add2),max(0,target3-count3-add3),max(0,target5-count5-(digit==5)),max(0,target7-count7-(digit==7)))
        def build_smallest(length,required):
            count2,count3,count5,count7=required
            answer=[]
            for position in range(length):
                remaining=length-position-1
                for digit in range(1, 10):
                    add2,add3=digit_factors.get(digit,(0,0))
                    new2=max(0,count2-add2)
                    new3=max(0,count3-add3)
                    new5=max(0,count5-(digit==5))
                    new7=max(0,count7-(digit==7))
                    if minimum_digits(new2,new3,new5,new7)<=remaining:
                        answer.append(str(digit))
                        count2=new2
                        count3=new3
                        count5=new5
                        count7=new7
                        break
            return ''.join(answer)
        n=len(num)
        for i in range(n-1,-1,-1):
            if i>first_zero:
                continue
            for digit in range(int(num[i])+1,10):
                required=get_remaining(prefix2[i],prefix3[i],prefix5[i],prefix7[i],digit)
                remaining_length=n-i-1
                if minimum_digits(*required)<=remaining_length:
                    suffix=build_smallest(remaining_length,required)
                    return num[:i]+str(digit)+suffix
        required_digits=minimum_digits(target2,target3,target5,target7)
        length=max(n+1,required_digits)
        return build_smallest(length,(target2,target3,target5,target7))
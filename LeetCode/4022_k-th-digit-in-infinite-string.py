
class Solution:
    def kthDigit(self, k: int) -> int:
        if k < 10:
            return k
        d=1
        while True:
            total_digits=9*d*pow(10,d-1)
            if k>total_digits:
                k-=total_digits
                d+=1
            else:
                break
        
        x=total_digits//9
        k+=x-1
        N=k//(d*10)
        k=k%(d*10)
        parity=N%2
        N*=10

        num=k//d
        den=k%d

        if parity:
            N=N+9-num
        else:
            N=N+num

        return int(str(N)[den])

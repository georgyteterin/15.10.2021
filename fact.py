num=int(input())
if num==0:
    print(1)
elif num>0:
    fact=1
    for i in range (1, num+1):
        fact=fact*i
    print(fact)
elif num<0:
    print ("попробуйте заново, введите, пожалуйста, неотрицательно число")
start=int(input())
incr=int(input( ))
days=int(input())
incrr = 1 + incr/100
print("день:    1    популяция   ", start )
for i in range (2, days+1):
    start=start*incrr
    print("день:   ", i , "   популяция   ", start )
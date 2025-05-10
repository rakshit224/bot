def maxmin(num):
    maximum =max(num)
    minimum =min(num)
    return maximum,minimum
a=[1,5,4,5,3,54,32,5,2,1,5,4,5,3,54,32,5,2]
maxx,minn=maxmin(a)
print(f'maximum  value is {maxx}')
print(f'minimum value is {minn}')

def MaxNum(a):
    chain = 1
    maxchain = 1
    for i in range(len(a)-1):
        if a[i] == a[i+1]:
            chain += 1
            if i+1 == len(a)-1:
                if maxchain < chain:
                    maxchain = chain
        else:
            if maxchain < chain:
                maxchain = chain
            chain = 1
    return maxchain

array=[['y','c','c',]

def gcf(a,b):
    af = [] # list for factors of a
    bf =[]  #;ost for factors of b
    #get factors of a
    for i in range(1,a+1):
        if a % i ==0:
            af.append(i)
    #get factors of b
    for i in range(1,b+1): #int(b/2)+1 then append the number
        if b % i ==0:
            bf.append(i)
    print(a, af)
    print(b, bf)
    ## get common factors
    cf = []
    for i in af:
        if i in bf:
            cf.append(i)
    print("common factors", cf)
    abgcf = max(cf)
    print(a,b, abgcf)
    return abgcf



if __name__ == "__main__":
    gcf(60,360)

import mygcf


# fractions and decimals
# out of = divide
# 1/10 = 0.1 = one tenth
# 1/100 = 0.01 = one hundreth
# 1/1000 = 0.001 = one thousandenth

print(10**3)
print(10**2)
print(10**1)
print(10**0)
print(10**-1)
print(10**-2)
print(10**-3)

print("decimal to fraction")
print("#"*20)
# get the decimal number
digits = input("input a decimal less than zero: ")

# get the number of decimal places
exponent = len(digits)-1

# convert the input to a float

n = float(digits)

# use the exponent to get the numerator
# remember n is less than one

numerator = int(n* 10**exponent)

# use the exponet to get  denominator 

denominator = 10**exponent

# percent is first two decimal places

percent = n * 100

# output

print("the decimal is ", n)
print("the fraction is ", numerator, "/", denominator)
## get the gfc
ndgcf = mygcf.gcf(numerator,denominator)
print("GCF: ",ndgcf)
## print the reduced fraction
print("the reduced fraction is ", int(numerator/ndgcf), "/", int(denominator/ndgcf))
print("the percent is ", percent, "%")
# Introduction
# Day 1 - 30DaysOfPython Challenge

print(3 + 2)   # addition(+)
print(3 - 2)   # subtraction(-)
print(3 * 2)   # multiplication(*)
print(3 / 2)   # division(/)
print(3 ** 2)  # exponential(**) power 3^2 = 9 
print(3 % 2)   # modulus(%) remainder = numerator - (quotient * denominator) 3 - (1*2)
print(3 // 2)  # Floor division operator(//)

# Checking data types

print(type(10))                  # Int
print(type(3.14))                # Float
print(type(1 + 3j))              # Complex
print(type('Asabeneh'))          # String
print(type([1, 2, 3]))           # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple
print(type(3 == 3))              # Bool
print(type(3 >= 3))              # Bool

# int to float
x:int=10
print(x)

x=36.2
print(x)


y:int = 10
print(y)  

y = float(y)
print(y)  

y=float(4.2) 
print (y)

y:int=5000  #only works in python not java script cuz we already declared y and by mentioning y:int again it will throw error 
print(y)
a=100
print (a)

# Declare a variable and initialize it
f = 0
print(f)
# re-declaring the variable works
f = 'guru99'
print(f)

a="Guru"
b = 99
print (a+ str(b))

# Declare a variable and initialize it
f = 101
print (f)
# Global vs. local variables in functions

def someFunction():
# global f
    f = 'I am learning Python'
    print (f)
someFunction()
print (f)
print(f)

def numerical_derivative(f,x,h=0.0001):
    return (f(x+h)-f(x))/h

def f(x):
    return x**3


#Central Difference

def central_diffrence(f,x,h=0.0001):
    return (f(x+h)-f(x-h))/2*h

x = 3

print(numerical_derivative(f,x))

print("Central Difference Method:",central_diffrence(f,x))


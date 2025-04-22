# practical example of decorator

def decoratorFunction(func):
    def wrapperFunction(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapperFunction

@decoratorFunction
def add(x,y):
    return x+y

print(add(2,3))    
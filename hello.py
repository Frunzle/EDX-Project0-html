import math

def square(x):
    return x*x

def root(x):
    return math.sqrt(x)

def main():
    for i in range(5):
        print (f"{i} squared is {square(i)}")
        print (f"the root of {i} = {root(i)}")

if __name__ == "__main__":
    main()
"""Small learning repo: basics, calculator, wordcount."""
def is_even(a):
    if a%2==0:
        return True
    return False

def multiply(a,b):
    return a*b

def main():
    assert is_even(10) is True
    assert is_even(7) is False
    assert multiply(3,4) == 12
    print("My Name")
    print(1+2)
    print([1,2,3,4,5])
    for i in range(1,21):
        print(i)

if __name__ == "__main__":
    main()
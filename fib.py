## Hacky script so far

## Goals:
##  1. Convert fibonacci number base to decimal base
##  2. Convert decimal base to fibonacci number base? (might be difficult)
## 

fib_dict = {0: 0, 1: 1, 2: 1, }

## Fibonacci number format (for now):
## Simply a string: "10110" = a_1 + a_2 + a_4

def from_fib_dict(a_sub):
    ## recursive definiton + memoization == superior performance!
    if a_sub in fib_dict:
        return fib_dict[a_sub]
    else:
        temp1 = from_fib_dict(a_sub-1)
        temp2 = from_fib_dict(a_sub-2)
        new_val = temp1 + temp2
        fib_dict[a_sub] = new_val
        return new_val

def test_equivalency_two_fibs(fib_num1, fib_num2):
    ## Test if two fibonacci numbers are equivalent
    ## ie does 100 == 011 in fib number base
    dec1 = fib_to_dec(fib_num1)
    dec2 = fib_to_dec(fib_num2)
    if dec1 == dec2: 
        print(f"{fib_num1} is equivalent to {fib_num2}\n")
        return True
    print(f"{fib_num1} IS NOT EQUIVALENT TO {fib_num2}\n")
    return False


def fib_to_dec(fib_str):
    ## convert a number in fibonacci base to its corresponding value in decimal
    val = 0
    for i in range(len(fib_str)-1, -1, -1):
        ## walk backwards, from least significant bit to most significant bit!
        a_sub = len(fib_str) - 1 - i ## just for clarity

        val_inc = int(fib_str[i]) * from_fib_dict(a_sub)
        val += val_inc
        
    print(f"Fibonacci string: {fib_str} = {val}")
    return val

def compute_addition(fib_num1, fib_num2):
    ## "Cheat" method
    ## convert to decmial 
    dec1 = fib_to_dec(fib_num1)
    dec2 = fib_to_dec(fib_num2)
    temp = dec1 + dec2 
    print("Adding:")
    print(" ",fib_num1)
    print("+ ", fib_num2)
    print("--------------")
    print(temp)


(test_equivalency_two_fibs("1000", "0110"))

fib_to_dec("10300")
fib_to_dec("10101")

a = "10111001"
b = "0011111"

compute_addition(a, b)

ans = "11100130"
fib_to_dec(ans) 
### IT works! The weird add and hold 2's and then move the 2's around works!
## Hard to argue run-time tho? Forseeable that we get a bad case that causes a lot of 2's to emerge and we have to keep pushing down
## ie 1111111 + 11111111 ----> a lot of applying Jeffrey's formula

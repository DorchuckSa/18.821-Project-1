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

def trim_leading_zeros(fib_str):
    ## get rid of leading zeros!
    while True:
        if fib_str[0] == "0":
            fib_str = fib_str[1:]
        else:
            break 
    return fib_str


def to_zeck(fib_str):
    fib_list = list(fib_str)
    fib_list.insert(0, '0')
    # print('fib list is', fib_list)

    ## Now, we apply the standard transformations to make it into Zeckendorf representation
    ## Rules:
    ##      1. If there are two adjacent 1's, then that can be made into a 1 in the column to the left
    new_fib_str = "".join(fib_list)
    while "11" in new_fib_str:
        for i in range(len(fib_list)-1):
            if fib_list[i] == "1" and fib_list[i+1] == "1": ## upgrade!
                ## Can use Rule 1 here
                ## argument - does not overwrite a 1, because we 
                ## would have "upgraded" on the previous iteration if
                ## fib_list[i-1] has a "1" in it the fib_list[i-1] and fib_list[i] would upgrad fib_list[i-2]
                fib_list[i-1] = "1"
                fib_list[i] = "0"
                fib_list[i+1] = "0"
        
    ## After one pass through, should be in Zeck form!
    ## INCORRECT Assumption - example is 10111001
        new_fib_str = "".join(fib_list) ## now multiple passes

    new_fib_str = trim_leading_zeros(new_fib_str) 

    if not(test_equivalency_two_fibs(fib_str, new_fib_str)):
        print("NOT GOOD ZECK CONVERSION BROKEN")

    print(f"Orig: {fib_str} converts to Zeck: {new_fib_str} \n")
    
    return new_fib_str




def dec_to_fib_helper(decimal_num):
    print("called with", decimal_num)
    fib_list = []
    index = 0 
    if decimal_num == 0:
        return fib_
    while from_fib_dict(index) <= decimal_num:
        fib_list.insert(0, "0")
        index += 1
    fib_list[0] = "1"
    print("fib list is", fib_list)
    # print("index is", index)
    val_added = from_fib_dict(index-1)
    new_val = decimal_num - val_added
    
    if new_val == 0:
        ## base case!
        return fib_list

    back_half = dec_to_fib_helper(new_val)
    ## now how to combine the lists? 
    size = len(back_half)

    fib_list[len(fib_list)-size:] = back_half ## set the back half of fib_list!
    return fib_list


def dec_to_fib(decimal_num):
    ## Have to brute force? 
    ## Recursive?  Inclined to think there's a recursive way to do this
    # fib_list = []
    # index = 0 
    # if decimal_num == 0:
    #     return fib_
    # while from_fib_dict(index) < decimal_num:
    #     fib_list.insert(0, "0")
    #     index += 1
    # fib_list.insert(0, "1")
    # print("index is", index)
    
    # ## recursive!!
    # val_added = from_fib_dict(index)
    # new_val = decimal_num - val_added
    
    # if new_val == 0:
    #     ## base case!
    #     return fib_list

    # back_half = dec_to_fib(new_val)
    # ## now how to combine the lists? 
    # size = len(back_half)

    # fib_list[len(fib_list)-size:] = back_half ## set the back half of fib_list!
    fib_list = dec_to_fib_helper(decimal_num)

    fib_str = "".join(fib_list)

    print(f"Decimal value of {decimal_num} is {fib_str}")
    return fib_str


    




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

a_z = to_zeck(a)
b_z = to_zeck(b)
compute_addition(a, b)
compute_addition(a_z, b_z)


ans = "11100130"
fib_to_dec(ans) 
### IT works! The weird add and hold 2's and then move the 2's around works!
## Hard to argue run-time tho? Forseeable that we get a bad case that causes a lot of 2's to emerge and we have to keep pushing down
## ie 1111111 + 11111111 ----> a lot of applying Jeffrey's formula

five  = "100000"
seven = "101000"

dec_to_fib(5)
dec_to_fib(7)
dec_to_fib(1239021)
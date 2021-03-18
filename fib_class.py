class FibonacciNumberBase:
    fib_dict = {0: 0, 1: 1, 2: 1, }

    @staticmethod
    def from_fib_dict(index):
        ## recursive definiton + memoization == superior performance!
        if index in FibonacciNumberBase.fib_dict:
            return FibonacciNumberBase.fib_dict[index]
        else:
            temp1 = FibonacciNumberBase.from_fib_dict(index-1)
            temp2 = FibonacciNumberBase.from_fib_dict(index-2)
            new_val = temp1 + temp2
            FibonacciNumberBase.fib_dict[index] = new_val
            return new_val

    @staticmethod
    def fib_to_dec(fib_str):
        ## convert a number in fibonacci base to its corresponding value in decimal
        val = 0
        for i in range(len(fib_str)-1, -1, -1):
            ## walk backwards, from least significant bit to most significant bit!
            a_sub = len(fib_str) - 1 - i ## just for clarity

            val_inc = int(fib_str[i]) * FibonacciNumberBase.from_fib_dict(a_sub)
            val += val_inc
            
        # print(f"Fibonacci string: {fib_str} = {val}")
        return val    
    
    def to_zeck(self):
        ## Now, we apply the standard transformations to make it into Zeckendorf representation
        ## Rules:
        ##      1. If there are two adjacent 1's, then that can be made into a 1 in the column to the left
        ## must pad with zero!

        self.simplify_twos()
        # print("original value is", self.fib_list)
        self.pad_with_zeros(len(self.fib_list) + 1)
        new_fib_str = FibonacciNumberBase.list_to_str(self.fib_list)
        ## Fix the to zeck logic
        # print("BEFORE ZECK", self.fib_list)
        for i in range(len(self.fib_list)-1):
            if self.fib_list[i] == 1 and self.fib_list[i+1] == 1:
                # self.fib_list[i-1] += 1
                # self.fib_list[i] -= 1
                # self.fib_list[i+1] -= 1

                self.fib_list[i-1] = 1
                self.fib_list[i] = 0
                self.fib_list[i+1] = 0
        

        for i in range(len(self.fib_list)-2, -1, -1):
            if self.fib_list[i] == 1 and self.fib_list[i+1] == 1:
                # self.fib_list[i-1] += 1
                # self.fib_list[i] -= 1
                # self.fib_list[i+1] -= 1

                self.fib_list[i-1] = 1
                self.fib_list[i] = 0
                self.fib_list[i+1] = 0
        # print("AFTER ZECK", self.fib_ list)


        # while "11" in new_fib_str:
        #     for i in range(len(self.fib_list)-1):
        #         if self.fib_list[i] == 1 and self.fib_list[i+1] == 1: ## upgrade!
        #             ## Argument - does not overwrite a 1, because we 
        #             ## would have "upgraded" on the previous iteration if
        #             ## fib_list[i-1] has a "1" in it the fib_list[i-1] and fib_list[i] would upgrad fib_list[i-2]
        #             self.fib_list[i-1] = 1
        #             self.fib_list[i] = 0
        #             self.fib_list[i+1] = 0
            
        #     ## After one pass through, should be in Zeck form!
        #     ## INCORRECT Assumption - example is 10111001
        #     ## Should be 2 passes, not sure how to prove?
        #     new_fib_str = FibonacciNumberBase.list_to_str(self.fib_list)
        
        self.trim_zeros()
        self.set_zeroth_digit()

        ## check value
        new_val = FibonacciNumberBase.fib_to_dec(new_fib_str)
        if new_val != self.dec:
            print("new value is", new_val, "for new string", new_fib_str)
            print("original value is", str(self.dec), "for original string", self.fib_str)
            raise Error("Zeck transformation failed")

        new_fib_str = FibonacciNumberBase.list_to_str(self.fib_list)
        if "11" in new_fib_str:
            print("NOT IN ZECK NORMAL FORM")
            raise Error("Zeck transformation failed")


        zeck_str = FibonacciNumberBase.list_to_str(new_fib_str)
        # self.fib_str = zeck_str
        return zeck_str
        

    @staticmethod
    def list_to_str(fib_list):
        fib_str = "".join(list(map(str, fib_list)))
        return fib_str
    
    @staticmethod
    def str_to_list(fib_str):
        fib_list = list(map(int, list(fib_str)))
        return fib_list






    def __init__(self, fib_str):
        self.fib_str = fib_str
        self.dec = FibonacciNumberBase.fib_to_dec(fib_str)
        self.fib_list = list(map(int, list(fib_str)))
        self.zeckendorf = FibonacciNumberBase.to_zeck(self)

    def pad_with_zeros(self, length):
        ## Pad self.fib_list with 0's to align lengths for addition and subtraction
        while len(self.fib_list) < length:
            self.fib_list.insert(0, 0)

    def trim_zeros(self):
        ## Trim leading 0's from self.fib_list
        if 1 not in self.fib_list:
            ## Base Case: all 0's = value of 0
            self.fib_list = [0]
        elif self.fib_list[0] == 0:
            self.fib_list = self.fib_list[1:]
            self.trim_zeros()
    
    def simplify_twos(self):
        self.pad_with_zeros(len(self.fib_list) + 1)

        first_ones_place = len(self.fib_list) - 2
        zeros_place = len(self.fib_list) - 1

        ## Open Question: how many passes are needed?
        # while 2 in self.fib_list or 3 in self.fib_list:
        # for j in range(1):
        for i in range(len(self.fib_list)-2):
            if self.fib_list[i] >= 2:
                ## Formula: 2*a_n = a_n+1 + a_n-2
                self.fib_list[i] -= 2
                self.fib_list[i-1] += 1
                self.fib_list[i+2] += 1
        
        ## base case - the first 1's digit is a 2
        if self.fib_list[first_ones_place] >= 2:
            self.fib_list[first_ones_place] -= 2
            self.fib_list[first_ones_place - 2] += 1 ## -2 gets us the to fib value of 2
            # fib_list[first_ones_dig + 2 ]

        ## second base case - the 0th digit is a 2 or more
        ## 0th digit doesn't matter so set to 0!
        if self.fib_list[zeros_place] >= 2:
            self.fib_list[zeros_place] = 0
    

        self.trim_zeros()

        # print("self fib list", self.fib_list)
        # print("str list", str("".join(self.fib_list)))
        temp = FibonacciNumberBase.list_to_str(self.fib_list)
        value = self.fib_to_dec(temp)    
        if value != self.dec:
            print("VALUE HAS CHANGED IN SIMPLIFY TWOS")
            print("original value", self.dec, self.fib_str)
            print("new value", temp, self.fib_list)
            raise("ERROR: Simplify 2s")


    def set_zeroth_digit(self):
        self.fib_list[-1] = 0

    def un_zeck(self, index):
        self.fib_list[index] -= 1
        self.fib_list[index+1] += 1
        self.fib_list[index+2] += 1

    def __add__(self, other):
        self.to_zeck()
        other.to_zeck()

        new_size = max(len(self.fib_list), len(other.fib_list))
        self.pad_with_zeros(new_size)
        other.pad_with_zeros(new_size)

        new_fib_list = []
        for i in range(len(self.fib_list)):
            new_val = self.fib_list[i] + other.fib_list[i]
            new_fib_list.append(new_val)

        sum_fib = FibonacciNumberBase(FibonacciNumberBase.list_to_str(new_fib_list))
        # print("new fib list", new_fib_list)
        sum_fib.simplify_twos()
        sum_fib.to_zeck()
        sum_fib.fib_str = FibonacciNumberBase.list_to_str(sum_fib.fib_list)

        print()

        print(f"  {self.fib_str}  = {self.dec}")
        print(f"+ {other.fib_str} = {other.dec}")
        print("______________________________")
        print(f"  {sum_fib.fib_str} = {sum_fib.dec}")

        self.cleanup()
        other.cleanup()
        sum_fib.cleanup()

        return sum_fib

    def setup_sub_overlap(self, other):
        for i in range(len(self.fib_list)-2):
            if other.fib_list[i] == 0 and self.fib_list[i] >= 1:
                if self.fib_list[i+1] == 0:
                    ## NO NEED TO UNZECK if next val is 1, just use that! leave this as "free val"
                    self.un_zeck(i)
                elif self.fib_list[i+1] >= 1 and other.fib_list[i+1] >= 1:
                    self.un_zeck(i)
            elif other.fib_list[i] >= 1 and self.fib_list[i] == 0:
                print("SHOULD BE IMPOSSIBLE???")
            
    def __sub__(self, other):
        self.to_zeck()
        other.to_zeck()

        new_size = max(len(self.fib_list), len(other.fib_list))
        # print("new size is", new_size)
        # print(self.fib_str)
        # print(other.fib_str)

        self.pad_with_zeros(new_size)
        other.pad_with_zeros(new_size)

        self.setup_sub_overlap(other)
        # print("after setup")
        # print(self.fib_str)
        # print(other.fib_str)

        sub_list = []
        for i in range(len(self.fib_list)):
            new_val = self.fib_list[i] - other.fib_list[i] 
            sub_list.append(new_val)

        sub_fib = FibonacciNumberBase(FibonacciNumberBase.list_to_str(sub_list))
        sub_fib.simplify_twos()
        # print("sub fib fib list is", sub_fib.fib_list)
        sub_fib.to_zeck()
        sub_fib.fib_str = FibonacciNumberBase.list_to_str(sub_fib.fib_list)

        print()

        print(f"  {self.fib_str}  = {self.dec}")
        print(f"- {other.fib_str} = {other.dec}")
        print("-------------------------")
        print(f"  {sub_fib.fib_str} = {sub_fib.dec}")

        self.cleanup()
        other.cleanup()
        sub_fib.cleanup()

        return sub_fib

    @staticmethod
    def make_perfect_fib_base(perfect_fib_index):
        ## given a perfect fib number, return the Fibonacci Number Base representing that number
        ## by "10...0" with perfect_fib_index 0's
        fib_str = "1" + "0"*perfect_fib_index 
        return FibonacciNumberBase(fib_str)

    @staticmethod
    def simple_multiplication(m, n):
        ## note: m > n
        if n > m:
            (m, n) = (n, m) ## swap, make m greater
        terms = []
        for i in range(m+n-1, m-n, -2):
            terms.append(FibonacciNumberBase.make_perfect_fib_base(i))
        
        running_sum = FibonacciNumberBase("0") ## start with 0
        for j, next_term in enumerate(terms):
            if j %2 == 0:
                running_sum = running_sum + next_term
            else:
                running_sum = running_sum - next_term
        
        return running_sum

    def __mul__(self, other):
        ## Goal: make power set of all indice alignments. Then sum up all simple multiplication terms
        self.to_zeck()
        other.to_zeck()

        new_size = max(len(self.fib_list), len(other.fib_list))

        self.pad_with_zeros(new_size)
        other.pad_with_zeros(new_size)       

        S = dec_to_fib(0)
        rPrev = dec_to_fib(0)
        rCur = other
        temp = dec_to_fib(0)
        if self.fib_list[len(self.fib_list)-2] == 1:
            S = S + other
        
        for i in range(2, len(self.fib_list)):
            temp = rPrev + rCur
            # print('temp is', temp)

            if self.fib_list[len(self.fib_list)-i-1] == 1:
                S = S + temp
            rPrev = rCur
            rCur = temp

        print()

        print(f"  {self.fib_str}  = {self.dec}")
        print(f"* {other.fib_str} = {other.dec}")
        print("-------------------------")
        print(f"  {S.fib_str} = {S.dec}")

        self.cleanup()
        other.cleanup()
        S.cleanup()

        return S 




        # power_set = []

        # self.to_zeck()
        # other.to_zeck()

        # new_size = max(len(self.fib_list), len(other.fib_list))

        # self.pad_with_zeros(new_size)
        # other.pad_with_zeros(new_size)        
        
        # self_indices = []
        # other_indices = []
        # for i in range(len(self.fib_list)):
        #     if self.fib_list[i] == 1:
        #         self_indices.append(new_size-1-i)
        #     if other.fib_list[i] == 1:
        #         other_indices.append(new_size-1-i)
        
        # prod = FibonacciNumberBase("0") ## start with 0
        # for self_index in self_indices:
        #     for other_index in other_indices:
        #         inc_val = FibonacciNumberBase.simple_multiplication(self_index, other_index)
        #         prod = prod + inc_val
        


    def __eq__(self, other): 
        dec1 = self.fib_to_dec(fib_num1)
        dec2 = self.fib_to_dec(fib_num2)
        if dec1 == dec2: 
            return True
        return False 

    def __str__(self):
        return "FibonacciNumberBase: " + self.fib_str + " = " + str(self.dec)

    def cleanup(self):
        self.simplify_twos()
        self.to_zeck()
        self.trim_zeros()

def dec_to_fib_helper(decimal_num):
    fib_list = []
    index = 0 
    if decimal_num == 0:
        return ["0",]
    while FibonacciNumberBase.from_fib_dict(index) <= decimal_num:
        fib_list.insert(0, "0")
        index += 1
    fib_list[0] = "1"

    val_added = FibonacciNumberBase.from_fib_dict(index-1)
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
    ## Convert a decimal number into its corresponding value in Fibonnaci Number Base! 
    ## Recursive?  Inclined to think there's a recursive way to do this
    fib_list = dec_to_fib_helper(decimal_num)

    fib_str = "".join(fib_list)

    # print(f"Decimal value of {decimal_num} is {fib_str}")
    return FibonacciNumberBase(fib_str)



def main():
    seven = FibonacciNumberBase("11010110110110101")
    five = FibonacciNumberBase("100010111111011101")
    # twelve = (dec_to_fib(12))
    # three = (dec_to_fib(3))
    # temp = twelve * three 

    twentytwo = (dec_to_fib(22))
    thirtyone = (dec_to_fib(31))
    temp = twentytwo + thirtyone

    print(temp)


if __name__ == "__main__":
    main()
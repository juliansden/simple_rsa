import random
import sys

class OperationsModulusN(object):
    """docstring for OperationsModulusN"""
    def __init__(self,x,n):
        super(OperationsModulusN, self).__init__()
        self.x = x
        self.n = n

    def add(self):
        pass

    def sub(self):
        pass

    def mult(self):
        pass

    def inverse(self):
        pass

    def pow(self):
        pass


MAX_INT = 2147483647

def generate_random_bit(rand_int):
    return bin(rand_int)[-1]

def generate_random_prime():
    bit_string = '1'
    increment = 4
    for x in range(1,6):
        rand_int = random.randint(1,MAX_INT)
        new_bit = generate_random_bit(rand_int)
        print("Line 15: b_"+str(x+increment)+"|"+str(rand_int)+"|"+new_bit)
        bit_string += new_bit
        increment = increment - 2
    bit_string += '1'
    return int(bit_string,2)

def is_prime(n):
    k = 20
    tested_ints = []
    for x in range(0,k):
        a = random.randint(1,n-1)
        if a not in tested_ints:
            tested_ints.append(a)
            # if a**(n-1) % n != 1:
            #   return false
            pass

def main():
    p1 = generate_random_prime()
    print("Line 23:","p1="+str(p1))
    p2 = generate_random_prime()
    print("Line 25:","p2="+str(p2))

if __name__ == '__main__':
    main()
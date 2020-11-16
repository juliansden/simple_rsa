import random
import sys
import math

class OperationsModulusN(object):
    """docstring for OperationsModulusN"""
    def __init__(self,n):
        super(OperationsModulusN, self).__init__()
        self.n = n

    def add(self,a,b):
        pass

    def sub(self,a,b):
        pass

    def mult(self,a,b):
        pass

    def inverse(self,a):
        pass

    def fast_exp(self,a,x):
        if x == 0:
            return 1
        elif x == 1:
            return a
        elif x - (2 * (x//2)) == 0:
            return self.fast_exp(a*a, x/2)
        elif x - (2 * (x//2)) == 1:
            return a * self.fast_exp(a*a, (x-1)/2)

    def pow(self,a,x):
        z = self.fast_exp(a,x)
        return z - (self.n * (z//self.n))


MAX_INT = 2147483647

def generate_random_bit(rand_int):
    return bin(rand_int)[-1]

def generate_random_prime():
    bit_string = '1'
    increment = 4
    for x in range(1,6):
        rand_int = random.randint(1,MAX_INT)
        new_bit = generate_random_bit(rand_int)
        print("Line 49: b_"+str(x+increment)+"|"+str(rand_int)+"|"+new_bit)
        bit_string += new_bit
        increment = increment - 2
    bit_string += '1'
    return int(bit_string,2)

def is_prime(n):
    mod_n = OperationsModulusN(n)
    k = 20
    tested_ints = []
    while k > 0:
        a = random.randint(1,n-1)
        if a not in tested_ints:
            tested_ints.append(a)
            k -= 1
            if mod_n.pow(a,n-1) != 1:
                return [False,tested_ints]
    return [True,tested_ints]

def main():
    p1_prime = False
    print("Calculating p1...")
    while not p1_prime:
        p1 = generate_random_prime()
        print("Line 70:","p1="+str(p1))
        is_p1_prime = is_prime(p1)
        if is_p1_prime[0]:
            print("Line 73: "+str(p1)+"|"+str(is_p1_prime[1][0])+"|"+str(p1)+" is perhaps prime")
            p1_prime = True
        else:
            print("Line 75: "+str(p1)+"|"+str(is_p1_prime[1][-1])+"|"+str(p1)+" is not prime")
            print("Calculating new number...")
    print("")
    p2_prime = False
    print("Calculating p2...")
    while not p2_prime:
        p2 = generate_random_prime()
        print("Line 77:","p1="+str(p2))
        is_p2_prime = is_prime(p2)
        if is_p2_prime[0]:
            print("Line 80: "+str(p2)+"|"+str(is_p2_prime[1][0])+"|"+str(p2)+" is perhaps prime")
            p2_prime = True
        elif p2 == p1:
            print("Line 92: p1 = p2, calculating new number...")
        else:
            print("Line 82: "+str(p2)+"|"+str(is_p2_prime[1][-1])+"|"+str(p2)+" is not prime")
            print("Calculating new number...")

if __name__ == '__main__':
    main()
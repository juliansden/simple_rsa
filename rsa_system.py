import random
import sys
import math

class OperationsModulusN(object):
    """docstring for OperationsModulusN"""
    def __init__(self,n):
        super(OperationsModulusN, self).__init__()
        self.n = n

    def mod(self,a,b):
        if a < b:
            return a
        elif a == b:
            return 0
        else:
            return a - (b * (a//b))

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
        elif self.mod(x,2) == 0:
            return self.fast_exp(a*a, x/2)
        elif self.mod(x,2) == 1:
            return a * self.fast_exp(a*a, (x-1)/2)

    def pow(self,a,x):
        z = self.fast_exp(a,x)
        return self.mod(z,self.n)

MAX_INT = 2147483647
PRIMES = [
    2,3,5,7,11,13,17,19,23,
    29,31,37,41,43,47,53,59,
    61,67,71,73,79,83,89,97,
    101,103,107,109,113,127
]

def generate_random_bit(rand_int):
    return bin(rand_int)[-1]

def generate_random_prime():
    bit_string = '1'
    increment = 4
    for x in range(1,6):
        rand_int = random.randint(1,MAX_INT)
        new_bit = generate_random_bit(rand_int)
        print("Line 62: b_"+str(x+increment)+"|"+str(rand_int)+"|"+new_bit)
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

def ext_euclid(a,b,mod_op):
    if a == 0:
        return b,0,1
    gcd,x1,y1 = ext_euclid(mod_op.mod(b,a),a,mod_op)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def find_key_pair(p,q,mod_op):
    phi_n = (p-1)*(q-1)
    e = PRIMES[0]
    i = 0
    found_e = False
    while not found_e:
        print("e="+str(e))
        gcd,x,y = ext_euclid(phi_n,e,mod_op)
        print("gcd="+str(gcd))
        if gcd == 1:
            print("found good e...")
            found_e = True
        else:
            print("trying new e...")
            i += 1
            e = PRIMES[i]
    if y < 0:
        return [[p*q,e],[p*q,(-1)*y]]
    else:
        return [[p*q,e],[p*q,y]]


def main():
    p1_prime = False
    print("Calculating p1...")
    while not p1_prime:
        p1 = generate_random_prime()
        print("Line 116:","p1="+str(p1))
        is_p1_prime = is_prime(p1)
        if is_p1_prime[0]:
            print("Line 119: "+str(p1)+"|"+str(is_p1_prime[1][0])+"|"+str(p1)+" is perhaps prime")
            p1_prime = True
        else:
            print("Line 122: "+str(p1)+"|"+str(is_p1_prime[1][-1])+"|"+str(p1)+" is not prime")
            print("Calculating new number...")
    print("")
    p2_prime = False
    print("Calculating p2...")
    while not p2_prime:
        p2 = generate_random_prime()
        print("Line 104:","p1="+str(p2))
        is_p2_prime = is_prime(p2)
        if is_p2_prime[0]:
            print("Line 132: "+str(p2)+"|"+str(is_p2_prime[1][0])+"|"+str(p2)+" is perhaps prime")
            p2_prime = True
        elif p2 == p1:
            print("Line 135: p1 = p2, calculating new number...")
        else:
            print("Line 137: "+str(p2)+"|"+str(is_p2_prime[1][-1])+"|"+str(p2)+" is not prime")
            print("Calculating new number...")
    print("")
    mod_op = OperationsModulusN((p1-1)*(p2-1))
    print("key pair:",str(find_key_pair(p1,p2,mod_op)[0]), str(find_key_pair(p1,p2,mod_op)[1]))

if __name__ == '__main__':
    main()
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
        if self.mod(a*a,self.n) == 1 and a != 1 and a != self.n-1:
            return False
        if x == 0:
            return 1
        elif x == 1:
            return a
        elif self.mod(x,2) == 0:
            return self.mod(self.fast_exp(a*a, x/2),self.n)
        elif self.mod(x,2) == 1:
            return self.mod(a * self.fast_exp(a*a, (x-1)/2),self.n)

    def pow(self,a,x):
        z = self.fast_exp(a,x)
        if not z:
            return z
        else:
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
    print("Line 64:")
    for x in range(1,6):
        rand_int = random.randint(1,MAX_INT)
        new_bit = generate_random_bit(rand_int)
        print("b_"+str(x+increment)+"|"+str(rand_int)+"|"+new_bit)
        bit_string += new_bit
        increment = increment - 2
    bit_string += '1'
    leading_zeros = "000000000000000000000000000"
    leading_zeros += bit_string
    print("Number|"+str(int(leading_zeros,2))+"|"+leading_zeros)
    print("")
    return int(leading_zeros,2)

def is_prime(n):
    mod_n = OperationsModulusN(n)
    k = 20
    tested_ints = []
    while k > 0:
        a = random.randint(1,n-1)
        if a not in tested_ints:
            tested_ints.append(a)
            k -= 1
            if not mod_n.pow(a,n-1):
                return [False,a]
            elif mod_n.pow(a,n-1) != 1:
                return [False,tested_ints]
    return [True,tested_ints]

def ext_euclid(a,b,mod_op,i,qi,si,ti):
    if i == 2:
        print("|"+str(i)+"\t|"+str(a//b)+"\t|"+str(a)+"\t|"+str(b)+"\t|"+str(a-(a//b)*b)+"\t|"+str(1)+"\t|"+str(0))
        qi.append(a//b)
        si.append(1)
        ti.append(0)
    elif i == 1:
        print("|"+str(i)+"\t|"+str(a//b)+"\t|"+str(a)+"\t|"+str(b)+"\t|"+str(a-(a//b)*b)+"\t|"+str(0)+"\t|"+str(1))
    else:
        print("|"+str(i)+"\t|"+str(a//b)+"\t|"+str(a)+"\t|"+str(b)+"\t|"+str(a-(a//b)*b)+"\t|"+str(si[-2]-(qi[-2]*si[-1]))+"\t|"+str(ti[-2]-(qi[-2]*ti[-1])))
        qi.append(a//b)
        si.append(si[-2]-(qi[-2]*si[-1]))
        ti.append(ti[-2]-(qi[-2]*ti[-1]))
    if a == 0:
        return b,0,1
    gcd,x1,y1 = ext_euclid(mod_op.mod(b,a),a,mod_op,i+1,qi,si,ti)
    x = y1 - (b//a) * x1
    y = x1
    return gcd,x,y

def find_key_pair(p,q,mod_op):
    phi_n = (p-1)*(q-1)
    e = PRIMES[0]
    i = 0
    found_e = False
    print("Line 117:")
    print("phi_n = "+str(phi_n))
    while not found_e:
        print("e="+str(e))
        print("i\t|qi\t|r\t|ri+1\t|ri+2\t|si\t|ti")
        gcd,x,y = ext_euclid(phi_n,e,mod_op,1,[phi_n//e],[0],[1])
        if gcd == 1:
            print("found good e...")
            print("")
            found_e = True
        else:
            print("trying new e...")
            i += 1
            e = PRIMES[i]
    print("Line 129:")
    if y < 0:
        print("d = "+str((-1)*y))
        return [[p*q,e],[p*q,(-1)*y]]
    else:
        print("d = "+str(y))
        return [[p*q,e],[p*q,y]]

def construct_r(name,n,e):
    

def main():
    # Part 1
    p1_prime = False
    print("Calculating p1...")
    while not p1_prime:
        p1 = generate_random_prime()
        print("Line 146:")
        is_p1_prime = is_prime(p1)
        if is_p1_prime[0]:
            print(str(p1)+" is perhaps prime")
            p1_prime = True
        elif isinstance(is_p1_prime[1],list):
            print("n="+str(p1),"a="+str(is_p1_prime[1][-1]))
            print(str(p1)+" is not prime because "+str(is_p1_prime[1][-1])+"^"+str(p1-1)+" mod " + str(p1)+" != 1")
            print("Calculating new number...")
        else:
            print("n="+str(p1),"a="+str(is_p1_prime[1]))
            print(
                str(p1)+" is not prime because "+str(is_p1_prime[1])+"^2 mod "+str(p1)+"=1 and "+
                str(is_p1_prime[1])+" != 1 and "+str(is_p1_prime[1])+" != "+str(p1-1))
            print("Calculating new number...")
    print("")
    p2_prime = False
    print("Calculating p2...")
    while not p2_prime:
        p2 = generate_random_prime()
        print("Line 166:")
        is_p2_prime = is_prime(p2)
        if is_p2_prime[0]:
            print(str(p2)+" is perhaps prime")
            p2_prime = True
        elif p2 == p1:
            print("p1 = p2, calculating new number...")
        elif isinstance(is_p2_prime[1],list):
            print("n="+str(p2),"a="+str(is_p2_prime[1][-1]))
            print(str(p2)+" is not prime because "+str(is_p2_prime[1][-1])+"^"+str(p2-1)+" mod " + str(p2)+" != 1")
            print("Calculating new number...")
        else:
            print("n="+str(p2),"a="+str(is_p2_prime[1]))
            print(
                str(p2)+" is not prime because "+str(is_p2_prime[1])+"^2 mod "+str(p2)+"=1 and "+
                str(is_p2_prime[1])+" != 1 and "+str(is_p2_prime[1])+" != "+str(p2-1))
            print("Calculating new number...")
    print("")
    mod_op = OperationsModulusN((p1-1)*(p2-1))
    pubk,privk = find_key_pair(p1,p2,mod_op)
    print("key pair:",str(pubk), str(privk))
    print("")

    # Part 2
    print("Line 190:")
    print("p="+str(p1),"q="+str(p2),"n="+str(pubk[0]),"e="+str(pubk[1]),"d="+str(privk[1]))
    print("p="+'{:032b}'.format(p1))
    print("q="+'{:032b}'.format(p2))
    print("n="+'{:032b}'.format(pubk[0]))
    print("e="+'{:032b}'.format(pubk[1]))
    print("d="+'{:032b}'.format(privk[1]))

if __name__ == '__main__':
    main()
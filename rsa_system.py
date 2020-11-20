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
    r = ""
    bin_name = ""
    for c in name:
        bin_name += bin(ord(c))[2:]
    for x in range(0,(6*8)-len(bin_name)):
        r += '0'
    r += bin_name
    for x in range(0,(4*8)-len(n)):
        r += '0'
    r += n
    for x in range(0,(4*8)-len(e)):
        r += '0'
    r += e
    print("r = "+str(r))
    return r

def h(r,e,construct_r):
    if construct_r:
        r1 = r[0:8]
        r2 = r[8:16]
        r3 = r[16:24]
        r4 = r[24:32]
        r5 = r[32:40]
        r6 = r[48:56]
        r7 = r[56:64]
        r8 = r[64:72]
        r9 = r[72:80]
        r10 = r[80:88]
        r11 = r[88:96]
        r12 = r[96:104]
        r13 = r[104:112]

        new_bit_string = '{:08b}'.format(int(r1,2)^int(r2,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r3,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r4,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r5,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r6,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r7,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r8,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r9,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r10,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r11,2))
        new_bit_string = '{:08b}'.format(int(new_bit_string,2)^int(r12,2))
        new_bit_string = '{:032b}'.format(int(new_bit_string,2)^int(r13,2))

        print("h(r) = "+new_bit_string)
        return new_bit_string
    else:
        s = '{:032b}'.format(int(r,2)^e)
        print("s = "+s)
        return s

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
    # Create Trent's keys
    print("******* CREATING TRENT KEYS *******")
    p1_prime = False
    p2_prime = False
    while not p1_prime:
        trent_p1 = generate_random_prime()
        is_p1_prime = is_prime(trent_p1)
        if is_p1_prime[0]:
            p1_prime = True
    while not p2_prime:
        trent_p2 = generate_random_prime()
        is_p2_prime = is_prime(trent_p2)
        if is_p2_prime[0]:
            p2_prime = True
    mod_op = OperationsModulusN((trent_p1-1)*(trent_p2-1))
    trent_pubk,trent_privk = find_key_pair(trent_p1,trent_p2,mod_op)
    print("******* END OF CREATING TRENT KEYS *******")
    print("")

    print("Line 190:")
    print("p="+str(p1),", q="+str(p2),", n="+str(pubk[0]),", e="+str(pubk[1]),", d="+str(privk[1]))
    print("p="+'{:032b}'.format(p1))
    print("q="+'{:032b}'.format(p2))
    print("n="+'{:032b}'.format(pubk[0]))
    print("e="+'{:032b}'.format(pubk[1]))
    print("d="+'{:032b}'.format(privk[1]))
    print("")
    print("Line 213:")
    h_r = h(construct_r('Alice','{:032b}'.format(pubk[0]),'{:032b}'.format(pubk[1])),0,True)
    s = h(h_r,trent_pubk[1],False)
    print("")
    print("Line 273:")
    print("h(r) = "+str(int(h_r,2)),", s = "+str(int(s,2)))
    print("")

if __name__ == '__main__':
    main()
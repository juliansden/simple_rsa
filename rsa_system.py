import random
import sys
import math

class OperationsModulusN(object):
    """
    This class handles all the operations modulus some positive integer n.
    n -> the number that all mod operations will use.
    """
    def __init__(self,n):
        super(OperationsModulusN, self).__init__()
        self.n = n
        self.square_fail_number = 0

    """Compute a % b."""
    def mod(self,a,b):
        if isinstance(a,list):
            return a
        if a < b:
            return a
        elif a == b:
            return 0
        else:
            return a - (b * (a//b))

    """Compute (a * b) % n."""
    def mult(self,a,b):
        return self.mod(a*b,self.n)

    """Use fast exponentiation to compute a**x mod n."""
    def fast_exp(self,a,x):
        print("Line 26:")
        print('{:<6s}{:<6s}{:<6s}{:<6s}'.format("|i","|xi","|y","|y"))
        k = len(bin(x))-3
        bin_x = bin(x)[2:]
        y = 1
        for i in range(0,k+1):
            if int(bin_x[i]) == 0:
                print('{:<6s}{:<6s}{:<6s}{:<6s}'.format("|"+str(len(bin_x)-i-1),"|"+str(bin_x[i]),"|"+str(self.mult(y,y)),"|"+str(self.mult(y,y))))
            y = self.mult(y,y)
            if int(bin_x[i]) == 1:
                print('{:<6s}{:<6s}{:<6s}{:<6s}'.format("|"+str(len(bin_x)-i-1),"|"+str(bin_x[i]),"|"+str(y),"|"+str(self.mult(a,y))))
                y = self.mult(a,y)
        print("")
        return y

    """Helper function for fast exponentiation."""
    def pow(self,a,x):
        return self.mod(self.fast_exp(a,x),self.n)

MAX_INT = 2147483647
PRIMES = [
    2,3,5,7,11,13,17,19,23,
    29,31,37,41,43,47,53,59,
    61,67,71,73,79,83,89,97,
    101,103,107,109,113,127
]

def generate_random_bit(rand_int):
    return bin(rand_int)[-1]

def generate_random_bitstring(no_prime):
    print("Line 50:")
    bit_string = '1'
    increment = 4
    if no_prime:
        for x in range(1,6):
            if x == 5:
                print("b_"+str(x+increment)+"|0|0")
            else:
                print("b_"+str(x+increment)+"|1|1")
            increment = increment - 2
        print("Number|"+str(int('0000000000000000000000000001111101',2))+"|0000000000000000000000000001111101")
        print("")
        return int('0000000000000000000000000001111101',2)
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
    print('{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}'.format("|i","|xi","|z","|y","|y"))
    mod_n = OperationsModulusN(n)
    k = 20
    tested_ints = []
    while k > 0:
        a = random.randint(1,n-1)
        if a not in tested_ints:
            tested_ints.append(a)
            nm1_bin = bin(n-1)
            y = 1
            a = 20
            for i in range(0,len(nm1_bin)-2):
                z = y
                y = mod_n.mult(y,y)
                if y == 1 and z != 1 and z != (n-1):
                    return [False,tested_ints,z]
                if int(nm1_bin[i+2]) == 1:
                    if len(tested_ints) == 1:
                        print('{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}'.format("|"+str(len(nm1_bin)-3-i),"|"+str(nm1_bin[i+2]),"|"+str(z),"|"+str(y),"|"+str(mod_n.mult(y,a))))
                    y = mod_n.mult(y,a)
                else:
                    if len(tested_ints) == 1:
                        print('{:<5s}{:<5s}{:<5s}{:<5s}{:<5s}'.format("|"+str(len(nm1_bin)-3-i),"|"+str(nm1_bin[i+2]),"|"+str(z),"|"+str(y),"|"+str(y)))
            if y != 1:
                return [False,tested_ints]
            k -= 1
    print("")
    return [True,tested_ints]

def ext_euclid(a,b,mod_op,i,qi,si,ti):
    if i == 2:
        print('{:<10s}{:<10s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}'.format("|"+str(i),"|"+str(a//b),"|"+str(a),"|"+str(b),"|"+str(a-(a//b)*b),"|"+str(1),"|"+str(0)))
        qi.append(a//b)
        si.append(1)
        ti.append(0)
    elif i == 1:
        print('{:<10s}{:<10s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}'.format("|"+str(i),"|"+str(a//b),"|"+str(a),"|"+str(b),"|"+str(a-(a//b)*b),"|"+str(0),"|"+str(1)))
    else:
        print('{:<10s}{:<10s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}'.format("|"+str(i),"|"+str(a//b),"|"+str(a),"|"+str(b),"|"+str(a-(a//b)*b),"|"+str(si[-2]-(qi[-2]*si[-1])),"|"+str(ti[-2]-(qi[-2]*ti[-1]))))
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
    print("Line 130:")
    print("phi_n = "+str(phi_n))
    while not found_e:
        print("e="+str(e))
        print('{:<10s}{:<10s}{:<12s}{:<12s}{:<12s}{:<12s}{:<12s}'.format('i','|qi','|r','|ri+1','|ri+2','|si','|ti'))
        gcd,x,y = ext_euclid(phi_n,e,mod_op,1,[phi_n//e],[0],[1])
        if gcd == 1 and (y < 0 and mod_op.mult(e,(-1)*y) == 1) or (y > 0 and mod_op.mult(e,y) == 1):
            print("found good e...")
            print("")
            found_e = True
        else:
            print("trying new e...")
            i += 1
            e = PRIMES[i]
    print("Line 144:")
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

def h(r,b):
    if b == 14:
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
        byte_strings = []
        for i in range(0,b):
            byte_strings.append(r[i*8:8*(i+1)])
        byte1 = int(byte_strings[0],2)
        for i in range(1,len(byte_strings)):
            byte1 = byte1^int(byte_strings[i],2)
        return byte1

def main():
    # Part 1
    p1_prime = False
    print("Calculating p1...")
    while not p1_prime:
        p1 = generate_random_bitstring(False)
        print("Line 215:")
        is_p1_prime = is_prime(p1)
        if is_p1_prime[0]:
            print(str(p1)+" is perhaps prime")
            p1_prime = True
        elif len(is_p1_prime) == 3:
            print("n="+str(p1),"a="+str(is_p1_prime[1]))
            print(
                str(p1)+" is not prime because "+str(is_p1_prime[1])+"^2 mod "+str(p1)+"=1 and "+
                str(is_p1_prime[1])+" != 1 and "+str(is_p1_prime[1])+" != "+str(p1-1))
            print("Calculating new number...")
        elif isinstance(is_p1_prime[1],list):
            print("n="+str(p1),"a="+str(is_p1_prime[1][-1]))
            print(str(p1)+" is not prime because "+str(is_p1_prime[1][-1])+"^"+str(p1-1)+" mod " + str(p1)+" != 1")
            print("Calculating new number...")
        
    print("")
    p2_prime = False
    print("Calculating p2...")
    no_prime = True
    while not p2_prime:
        p2 = generate_random_bitstring(no_prime)
        no_prime = False
        print("Line 238:")
        is_p2_prime = is_prime(p2)
        if is_p2_prime[0] and p2 != p1:
            print(str(p2)+" is perhaps prime")
            p2_prime = True
        elif p2 == p1:
            print("p1 = p2, calculating new number...")
        elif len(is_p2_prime) == 3:
            print("n="+str(p2),"a="+str(is_p2_prime[1]))
            print(
                str(p2)+" is not prime because "+str(is_p2_prime[1])+"^2 mod "+str(p2)+"=1 and "+
                str(is_p2_prime[1])+" != 1 and "+str(is_p2_prime[1])+" != "+str(p2-1))
            print("Calculating new number...")
        elif isinstance(is_p2_prime[1],list):
            print("n="+str(p2),"a="+str(is_p2_prime[1][-1]))
            print(str(p2)+" is not prime because "+str(is_p2_prime[1][-1])+"^"+str(p2-1)+" mod " + str(p2)+" != 1")
            print("Calculating new number...")
    print("")
    mod_op = OperationsModulusN((p1-1)*(p2-1))
    pubk,privk = find_key_pair(p1,p2,mod_op)
    print("ALICE key pair:",str(pubk), str(privk))
    print("")

    # Part 2
    # Create Trent's keys
    print("******* CREATING TRENT KEYS *******")
    p1_prime = False
    p2_prime = False
    while not p1_prime:
        trent_p1 = generate_random_bitstring(False)
        is_p1_prime = is_prime(trent_p1)
        if is_p1_prime[0]:
            p1_prime = True
    while not p2_prime:
        trent_p2 = generate_random_bitstring(False)
        is_p2_prime = is_prime(trent_p2)
        if is_p2_prime[0]:
            p2_prime = True
    mod_op = OperationsModulusN((trent_p1-1)*(trent_p2-1))
    trent_pubk,trent_privk = find_key_pair(trent_p1,trent_p2,mod_op)
    print("TRENT KEYS: ", trent_pubk, trent_privk)
    print("******* END OF CREATING TRENT KEYS *******")
    print("")

    print("Line 282:")
    print("Alice key values are below...")
    print("p="+str(p1),", q="+str(p2),", n="+str(pubk[0]),", e="+str(pubk[1]),", d="+str(privk[1]))
    print("p="+'{:032b}'.format(p1))
    print("q="+'{:032b}'.format(p2))
    print("n="+'{:032b}'.format(pubk[0]))
    print("e="+'{:032b}'.format(pubk[1]))
    print("d="+'{:032b}'.format(privk[1]))
    print("")
    print("Line 291:")
    mod_op = OperationsModulusN(trent_pubk[0])
    h_r = h(construct_r('Alice','{:032b}'.format(pubk[0]),'{:032b}'.format(pubk[1])),14)
    s = mod_op.pow(int(h_r,2),trent_pubk[1])
    print("s = "+str('{:032b}'.format(s)))
    print("")
    print("Line 297:")
    print("h(r) = "+str(int(h_r,2)),", s = "+str(s))
    print("")

    # Part 3
    k = bin(pubk[0])[2:]
    leading_zeros = ""
    for i in range(0,32-len(k)):
        leading_zeros += "0"
    new_bits = "1"
    for i in range(1,len(k)-1):
        new_bits += bin(random.randint(1,MAX_INT))[-1]
    new_bits += "1"
    u = leading_zeros + new_bits
    print("Line 311:")
    print("k =",int(k,2), ", u =",int(u,2))
    print("")
    print("Line 314:")
    print("u =",u)
    print("")
    h_u = h(u,len(u)//8)
    mod_op = OperationsModulusN(pubk[0])
    v = mod_op.pow(h_u,privk[1])
    e_v = mod_op.pow(v,pubk[1])
    print("Line 318:")
    print("u =",u,", h(u) =",h_u,", v =",v,", Ev =",e_v)
    print("")

if __name__ == '__main__':
    main()
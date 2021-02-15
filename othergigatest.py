#!/usr/bin/python 
import random
import argparse
def log_shift(val, num):
    if num == 0:
        return int(val)
    else:
        return int(abs(val / (2 * shift)))
def twos_comp(val):
    if ( val & (1 << 15)) != 0:
        val = val - (1 << 15)
    return val
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--adder', action = 'store_true')
parser.add_argument('-s', '--shifter', action = 'store_true')
parser.add_argument('-t', '--total', action = 'store_true')
parser.add_argument('-n', '--num')
args = parser.parse_args()
if args.adder:
    print("A<15:0> B<15:0> Cin --> S<15:0> Cout")
    for bored in range(int(args.num) + 1):
        a = random.randint(0,65535)
        b = random.randint(0,65535)
        c = random.randint(0,1)
        if a + b + c< 65536:
            print(hex(a), hex(b), hex(c), hex((a+b+c) % 65536), 0)
        else:
            print(hex(a), hex(b), hex(c), hex((a+b+c) % 65536), 1)

elif args.shifter:
    print("A<15:0> rshift<1:0> ars --> out<15:0>")
    for bored in range(int(args.num) +1):
        a = random.randint(0,65535)
        shift = random.randint(0,3)
        ars = random.randint(0,1)
        if ars:
            if a >= 32768:
                if shift == 0:
                    print(hex(a), hex(shift), hex(ars), hex(a >> shift))
                elif shift == 1:
                    print(hex(a), hex(shift), hex(ars), hex((a >> shift)+ 32768))
                elif shift == 2:
                    print(hex(a), hex(shift), hex(ars), hex((a >> shift) + 49152))
                else:
                    print(hex(a), hex(shift), hex(ars), hex((a >> shift)+ 57344))


            else:
                print(hex(a), hex(shift), hex(ars), hex(a >> shift))
        else:
            print(hex(a), hex(shift), hex(ars), hex(a >> shift))


elif args.total:
    print("rf_p1<15:0> rf_p0<15:0> src1_sel src0_sel rshft<1:0> ars Cin --> dst<15:0> Cout")
    rf_p1_old = 0
    rf_p0_old = 0

    for bored in range(int(args.num) +1):
        rf_p1 = random.randint(0, 65535)
        rf_p0 = random.randint(0, 65535)
        src1_sel = random.randint(0,1)
        src0_sel = random.randint(0,1)
        if bored == 0:
            src1_sel = 1
            src0_sel = 1
        rshift = random.randint(0,3)
        ars = random.randint(0,1)
        Cin = random.randint(0,1)
        #Compute rf_p1_shifted
        if ars:
            if rf_p1_old >= 32768:
                if rshift == 0:
                    rf_p1_shifted =rf_p1_old >> rshift
                elif rshift == 1:
                    rf_p1_shifted = rf_p1_old >> rshift+ 32768
                elif rshift == 2:
                    rf_p1_shifted = (rf_p1_old >> rshift) + 49152
                else:
                    rf_p1_shifted = (rf_p1_old >> rshift)+ 57344


            else:
                rf_p1_shifted = rf_p1_old >> rshift
        else:
           rf_p1_shifted = rf_p1_old >> rshift 
        sum =  (rf_p1_shifted + rf_p0_old + Cin) % 65536

        if rf_p1_shifted + rf_p0_old + Cin < 65536:
            Cout = 0
        else:
            Cout = 1
        if bored == 0:
            print(hex(rf_p1), hex(rf_p0), hex(src1_sel), hex(src0_sel), hex(rshift), hex(ars), hex(Cin), "XXXX", "x")
        else:
            print(hex(rf_p1), hex(rf_p0), hex(src1_sel), hex(src0_sel), hex(rshift), hex(ars), hex(Cin), hex(sum), hex(Cout))

        if src1_sel == 0:
            rf_p1_old = sum
        else:
            rf_p1_old = rf_p1
        if src0_sel == 0:
            rf_p0_old = sum
        else:
            rf_p0_old = rf_p0
 
    

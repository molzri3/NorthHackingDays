from z3 import *

s = Solver()

coupon = [BitVec(f"coupon_{i}", 8) for i in range(37)]

for c in coupon:
    s.add(c >= 32, c <= 126)  # Restrict to writable ASCII characters

s.add(coupon[1]+coupon[6]+coupon[3]+coupon[5]+coupon[14]+coupon[36] == 562)
s.add(coupon[35]+coupon[2]+coupon[33] == 245)
s.add(coupon[34]+coupon[26]+coupon[24] == 228)
s.add(coupon[28]+coupon[1]+coupon[36]+coupon[0]+coupon[21]+coupon[6]+coupon[16]+coupon[20] == 667)
s.add(coupon[34]+coupon[20]+coupon[34]+coupon[2]+coupon[12]+coupon[15] == 450)
s.add(coupon[23]+coupon[36]+coupon[8] == 323)
s.add(coupon[15]+coupon[13]+coupon[14]+coupon[16]+coupon[31]+coupon[3]+coupon[32]+coupon[15] == 748)
s.add(coupon[13]+coupon[2] == 120)
s.add(coupon[6]+coupon[23]+coupon[32]+coupon[0]+coupon[19] == 467)
s.add(coupon[15]+coupon[17]+coupon[36]+coupon[6]+coupon[26]+coupon[25] == 542)
s.add(coupon[13]+coupon[28]+coupon[26]+coupon[8] == 304)
s.add(coupon[23]+coupon[4]+coupon[19]+coupon[13]+coupon[11]+coupon[33] == 518)
s.add(coupon[23]+coupon[2] == 177)
s.add(coupon[21]+coupon[21]+coupon[1]+coupon[32]+coupon[6]+coupon[29]+coupon[14]+coupon[34]+coupon[34] == 780)
s.add(coupon[1]+coupon[16]+coupon[5]+coupon[34] == 258)
s.add(coupon[3]+coupon[17]+coupon[34]+coupon[1]+coupon[21]+coupon[36] == 616)
s.add(coupon[10]+coupon[28]+coupon[13]+coupon[31]+coupon[10]+coupon[33]+coupon[21]+coupon[14] == 662)
s.add(coupon[22]+coupon[27]+coupon[25]+coupon[18]+coupon[8] == 430)
s.add(coupon[11]+coupon[32]+coupon[28]+coupon[8]+coupon[35]+coupon[11] == 597)
s.add(coupon[24]+coupon[19]+coupon[32]+coupon[29]+coupon[15]+coupon[5]+coupon[27]+coupon[14] == 729)
s.add(coupon[25]+coupon[11] == 177)
s.add(coupon[31]+coupon[33]+coupon[26]+coupon[30]+coupon[14]+coupon[13]+coupon[19]+coupon[32]+coupon[11] == 797)
s.add(coupon[29]+coupon[20]+coupon[14] == 213)
s.add(coupon[4]+coupon[1] == 159)
s.add(coupon[5]+coupon[31]+coupon[28] == 280)
s.add(coupon[13]+coupon[32] == 147)
s.add(coupon[11]+coupon[16] == 147)
s.add(coupon[35]+coupon[1]+coupon[22]+coupon[9]+coupon[17]+coupon[12]+coupon[22]+coupon[9]+coupon[29] == 734)
s.add(coupon[18]+coupon[22]+coupon[36]+coupon[22] == 318)
s.add(coupon[32]+coupon[6]+coupon[8]+coupon[26]+coupon[27]+coupon[8]+coupon[26] == 566)
s.add(coupon[6]+coupon[11]+coupon[11]+coupon[6]+coupon[7]+coupon[27]+coupon[29]+coupon[12]+coupon[22] == 681)
s.add(coupon[7]+coupon[35]+coupon[23] == 272)
s.add(coupon[6]+coupon[2]+coupon[12] == 216)
s.add(coupon[19]+coupon[26]+coupon[1]+coupon[27]+coupon[0]+coupon[19]+coupon[5] == 586)
s.add(coupon[28]+coupon[10]+coupon[31]+coupon[18]+coupon[21]+coupon[17] == 586)
s.add(coupon[34]+coupon[30] == 181)
s.add(coupon[1]+coupon[12]+coupon[14]+coupon[8]+coupon[28]+coupon[5] == 511)

if s.check() == sat:
    m = s.model()
    b = "".join(chr(m.eval(coupon[y]).as_long()) for y in range(37)).encode('UTF-8')
    print(b)
else:
    print("No solution found")



#NHD{W4L4Yn1_H4rb4n_m0h1m_R3sp3ct_BRo}

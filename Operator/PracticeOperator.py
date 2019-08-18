# a = 20; b= 30;
#
# a += b
# print a
#
# print a is b
# print a is not b
#
# a = [10, 20, 30]
# print 10 in a
# print 50 not in a

a=b = 3
print a
print b




# no = 64

#       2 < 56
# 2*2 = 4 <56
# 4*2 = 8 < 56
# 8*2 = 16 <56
# 16*2 =32 <56
# 32*2 = 64<56 (false loop brake)
# 64 == 56 print 56 is multiple of 2
# 64>56 print 56 is not multiple of 2
# no=2
# while no < 5000:
#     print "test for" + str(no)
#     m2 = 2
#     result1 = None
#     result2 = None
#     while m2 < no:
#         m2 = m2 * 2
#     if m2 == no:
#         result1 = "no is multiple 2"
#         print "no is multiple 2"
#     elif m2>no:
#         result1 = "no is not multiple of 2"
#         print "no is not multiple of 2"
#
#     # only in el
#     #
#     # 2 === 000000000000010 == 01
#     # 4 === 100 == 011
#     # 8 === 1000 == 0111
#     # 16 === 10000 == 01111
#
#     # 56 11100
#     if no & (no-1)  == 0:
#         result2 = "no is multiple 2"
#         print "no is multiple 2"
#     else:
#         result2 = "no is not multiple of 2"
#         print "no is not multiple of 2"
#     if result1 != result2:
#         print "logic fails"
#         break
#     no = no + 1

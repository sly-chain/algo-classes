def karatsuba(x,y):
    """Function to multiply 2 numbers in a more efficient manner than the 
    grade school algorithm"""
    
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y
    
    else:
        str_x = str(x)
        str_y = str(y)
        n = max(len(str_x),len(str_y))
        nby2 = int(n / 2)
		
        a = int(str_x[0:nby2])
        b = int(str_x[-nby2:])
        c = int(str_y[0:nby2])
        d = int(str_y[-nby2:])
		
        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
    # this little trick, writing n as 2*nby2 takes care of both even and odd n
        prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
        print("print", ac, ad_plus_bc, bd)
        
        return prod
    
    
# =============================================================================
# procedure karatsuba(num1, num2)
#   if (num1 < 10) or (num2 < 10)
#     return num1*num2
        
#   /* calculates the size of the numbers */
#   m = max(size_base10(num1), size_base10(num2))
#   m2 = m/2
        
#   /* split the digit sequences about the middle */
#   high1, low1 = split_at(num1, m2)
#   high2, low2 = split_at(num2, m2).
        
#   /* 3 calls made to numbers approximately half the size */
#   z0 = karatsuba(low1,low2)
#   z1 = karatsuba((low1+high1),(low2+high2))
#   z2 = karatsuba(high1,high2)
        
#   return (z2*10^(2*m2))+((z1-z2-z0)*10^(m2))+(z0)
# =============================================================================


#x = 3141592653589793238462643383279502884197169399375105820974944592
#y = 2718281828459045235360287471352662497757247093699959574966967627
#print(karatsuba(x,y))
        
print(karatsuba(1234, 5678))
#6454652
print(karatsuba(3, 11))
#33
print(karatsuba(12, 56))
#672
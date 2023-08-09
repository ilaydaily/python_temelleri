'''
Yarıçapı verilen bir dairenin alan ve çevresini hesaplayın
'''

pi = 3.14

r = float(input("yarı çap: "))
alan = pi * (r ** 2)
cevre = 2 * pi * r

print("alan: " + str(alan))  #string tipinde yazdır
print("cevre:", cevre)
name = 'Çınar'
surname = 'Turan'

# print('My name is {}{}'.format(name, surname))
#süslü parantez içine name&surname bilgisi gelecek ve yukarıdaki stringten alınacak
#parantez içindeki name ve surname süslü parantez içine gelecek olan argümandır

'''print('My name is {0} {1}'.format(name, surname))
#OUTPUT => Çınar Turan

print('My name is {1} {0}'.format(name, surname))
#OUTPUT => Turan Çınar
#index numaralarını değiştirince output da değişti'''

print('My name is {s}{n}'.format(n=name, s=surname))
#index numarası yerine değişkene isim verip bu şekilde de çağırabiliriz

print("My name is {} {} and I'm {} years old".format(name, surname, '36'))
## My name is Çınar Turan and I'm 36 years old

result = 200/500
print('The result is {}'.format(result))
## The result is 0.4

result2 = 200/700
print('The result2 is {r:1.4}'.format(r=result2))
##The result2 is 0.2867
#normalde sonuç 0.2857142857142857 ama 1.4 diyerek sadece 4'e kadar olan kısmını yazdırdık (virgülden sonra)
#buradaki 1 --> tam kısım için kaç karakter boşluk konulacağıdır
# 1 yerine 10 olsaydı '     0.28571' olurdu --> sayıyla birlikte toplam 10 karakterlik yer

age = 36
print(f"My name is {name} {surname} and I'm {age} years old")
#tırnağın başına f yazdığımız için parantezlerin içine direkt parametreleri verebildik
#böylece format kullanmadan outputta yazdırmış olduk

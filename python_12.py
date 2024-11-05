evens = []
odds = []
for n in range(10):
    if n % 2 == 0:
        evens. append(n)
    else:
        odds . append(n)
print(evens)
print (odds)

numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
evens = []
odds = []
for n in numbers:
    if n % 2 == 0:
        evens. append(n)
    else:
        odds. append(n)
print(evens)
print(odds)
print('Cift sayilarin adedi', len(evens))
print('Tek sayilarin adedi', len(odds))

numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
ciftler = 0
tekler = 0
for i in numbers:
    if i%2 == 0:
        ciftler+=1
    else:
        tekler+=1
print('Cift sayilarin adedi', ciftler)
print('Tek sayilarin adedi', tekler)

numbers = (11, 36, 33, 66, 89, 21, 32, 16, 10)
odds = 0
evens = 0
for i in numbers:
    if not i % 2:
        evens+=1
    else:
        odds+=1
print ("The number of even numbers :", evens)
print ("The number of odd numbers :", odds)

for i in range(1,10):
    print(str(i)*i)

for i in range(1, 10):
    print(str(i) * i)

'a'*5

toplam = 0
for i in range(1,75):
    toplam+=i
print(toplam)

sum(range(1,75))

sum_num=0
for i in range(1, 75):
    sum_num += i
print(sum_num)

who = ['I am ', 'You are ']
mood = ['happy' , 'confident' ]
for i in who:
    for ii in mood:
        print(i + ii)

a = ['a', 'b', 'c' ]
b = [1,2,3]
for i in a:
    for j in b:
        print(i,j)

names = ["susan", "tom", "edward"]
mood = ["happy", "sad"]
for name in names:
    for m in mood:
        print(f'{name} is {m}')
    
names = ["susan", "tom", "edward"]
mood = ["happy", "sad" ]
for i in names:
    for ii in mood:
        print(i + " is " + ii)

print('Say: I love you!')
print ()
print('me too', 2019)

# help(print)

listA = ["susan", "tom", False, 0, "0"]
filtered_list = filter(None, listA)
print("The filtered elements are : ")
for i in filtered_list:
    print(i)

listem = ['ali', [], 5, False, 3.14, '0']
list(filter(None, listem))

names = ["susan", "tom", "edward"]
list(enumerate(names))

for i,j in enumerate(names):
    print(i,j)

listem = list(enumerate(names))
for i, j in listem:
    print(i,j)

listem = list(enumerate(names,5))
for i, j in listem:
    print(i,j)

grocery = ['bread', 'water', 'olive' ]
enum_grocery = enumerate(grocery)
print(type(enum_grocery))
print(list(enum_grocery))
enum_grocery = enumerate(grocery, 10)
print(list(enum_grocery) )

number = [-222, 0, 16, 5, 10, 6]
largest_number = max(number)
smallest_number = min(number)
print("The largest number is:", largest_number)
print("The smallest number is:", smallest_number)

max([3,5,7,2,6,9,])
min([3,5,7,2,6,9,])


numbers = [2.5, 30, 4, -15]
numbers_sum = sum(numbers)
print(numbers_sum)
numbers_sum = sum(numbers, 20)
print(numbers_sum)

sum([3,5,7,2,6,9, ])
sum([3,5,7,2,6,9,],20)

def karesini_al(x):
    pass

def karesini_al(x):
    print(x ** 2)

karesini_al(5)
karesini_al(7)

def toplama():
    print('a'+5)

def hipotenus(a,b):
    print((a ** 2+b ** 2) ** 0.5)
hipotenus(3,4)

def multiply(a, b) :
    print (a * b)

multiply(3, 5)
multiply(-1, 2.5)
multiply('amazing ', 3) # it's really amazing, right?

def motto() :
    print("Don't hesitate to reinvent yourself!")
motto()# it takes no argument

def add(ahmet, yasin):
    print(ahmet+yasin)

add(5,7)
add('Nalan', "Python")

def add(a, b):
    print(a + b)
add(-3, 5)

def ciftmi(x):
    return x%2 == 0
print(ciftmi(6))
ciftmi(5)

listem = list(range(1,11))
listem

list(filter(ciftmi, listem))

listem

filtered = (filter(ciftmi, listem))

for i in filtered:
    print(i)

for i in filtered:
    print(i)

a = [1,2,3]
b = [5,6,7]
c = zip(a,b)

for i in c:
    print(i)

for i in c:
    print(i)

type(c)

a = [5,7,8,2,4,0]
e = enumerate(a, 15)
for i in e:
    print(i)

a = [1,2,3]
b = [5,6,7]
c = list(zip(a,b))

for i in c: 
    print(i)

for i in c: 
    print(i)

names
['susan', 'tom', 'edward']
list(map(len, names))

condition = (3 > 1) and (1 < 1)
if not condition:
    print('It works')
else:
    print('Something is wrong')

price = '2200'
if price <= '2200' :
    print('I can afford it')
else:
    print('It is expensive')

'a' < 'b'
'Z'<'a'

if 'bar' in {'foo' : 1, 'bar' : 2, 'baz' : 3, 'qux' : 4} :
    print (1)
    print (2)
    if 'a' in 'qux' :
        print (3)
print (4)

test = 155
if (test <= 200) :
    if (test < 100) :
        if (test <= 0) :
            print ("Ali")
        else:
            print ("Burak")
    else:
        print ("Selin")
else:
    print ("Demet")

def add(a, b):
    print(a + b)
add(-3, 5)

# hesap makinesi
def hesap(a,b,islem):
    if islem == '+':
        print(a+b)
    elif islem == '-':
        print(a-b)
    elif islem == '*':
        print(a*b)
    elif islem == '/':
        print(a/b)
    else:
        print('Geçersiz islem girdiniz. ')

hesap(3,5,"+")
hesap(3,5,"-")
hesap(5,3,"-")

# hesap makinesi
def hesap2(a,islem,b):
    if islem == '+':
        print(a+b)
    elif islem == '-':
        print(a-b)
    elif islem == '*':
        print(a*b)
    elif islem == '/':
        print(a/b)
    else:
        print('Geçersiz islem girdiniz. ')
hesap2(2, '*',7)

birinci = int(input('Birinici sayiyi giriniz'))
ikinci = int(input('ikinci sayiyi giriniz'))
islem = input('Yapmak istediğiniz islemi giriniz')
hesap(birinci, ikinci,islem)

def multiply_1(a, b) :
    print(a * b) # it prints something
multiply_1(10, 5)
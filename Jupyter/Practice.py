'''var1 = 10
var2 = 20
var3 = 30

#print(var1, var2, var3)
print(var1)
print(var2)
print(var3)

var1, var2, var3 = 10, 20, 30
#1      2     3     1   2   3
print(var1, var2, var3)

sr_no, name, age = 1, "John", 25

no = sr_no
client_name = name
age_of_client = age

#print("Our new client is ", client_name, "with the serial number ", no, "and age ", age_of_client)

var_test1 = sr_no
var_test2 = name
var_test3 = age

print(var_test1)
print(var_test2)
print(var_test3)'''

#Swap the values of two variables
'''a = 5
b = 10
print("Before swapping: a =", a, "b =", b)
a, b = b, a

print("After swapping: a =", a, "b =", b)'''

'''var1 = 'google launched new pixel "11" series in 2023'
var2 = "google launched new pixel '11' series in 2026"
print("second var: " , var2, ", first var:" , var1)

word = 'don\'t'
print(word)

#new line character
new_line = "Ram is good at\nsql and python"
print(new_line)

# \t = tab

str2 = "We are learning\t Data\t Engineering"
print(str2)

#ASCII values of characters
print("A:", ord("A"))
print("a:", ord("a"))
print("1:", ord("1"))
print("z:", ord("z"))
print("Z:", ord("Z"))'''

#chr()
#rint("chr(65):", chr(65))



'''li = [1,2,3,4,5]

for i in li:
    print(i*i)

li2 = [1,2,3,4,5,6,7,8,9,10]

i = len(li2) - 1

while i >= 0:
    if li2[i] == 8:
        print("Number of Iterator " + str(i))
    i += -1

userVal = int(input("Enter the Number :"))

val = userVal % 2

if val == 0:
    print("even Number")
elif val != 0:
    print("odd Number")'''


'''dict5 = {'name':['ram', 'akash'], 'age':25, 'location':'pune'}
print(dict5.keys())
for i in dict5.keys():
    print(i)

for i,j in dict5.items():
    print(i,':',j)'''

'''def isDelChargeApplicable(aiTotalPrice):
    finalPrice = 0
    if aiTotalPrice < 500:
         finalPrice = aiTotalPrice + (aiTotalPrice * 0.10)
    else:
        finalPrice = aiTotalPrice
    return finalPrice


liAmount2 = int(input("Enter_Amount : "))
payAmount = isDelChargeApplicable(liAmount2)
print("payAmount : ", payAmount )'''


'''li = [5,7,6,9,5,48,7]
try:
    for i in range(len(li) + 1):
        print('Value of li is :', li[i])
        i = i + 1
except Exception as e:
    print('exception occurred:', e)'''

data = {
    "name" : ["Akash", "Aniruddh", "Ashwin", "Ashish", "Ashok", "Alok", "Amar", "Ananta", "Aniket", "Anil", "Andrew", "Anna"],
    "age" : [34,32,21,54,12,34,23,15,35,29,19],
    "city" : [],
    "active" : []
}

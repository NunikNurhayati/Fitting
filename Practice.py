print("I am a chemist.")
print("She asked, \"What are you doing?\"")

tuna = 5
carrot = 7

print(tuna + carrot)
print(5 * 5)
print(5 ** 3)
print(18 / 4)
print(18%4)
print(2006500/128)
print(18//4)
print(17 + 05)
print(18/4)
print(5*3)
print("Why the result of 18/4 is 4 (bilangan bulat)?")
print("--------------------------------------------------")

print(2006500./128.)
print("\"Hey, what are you doing?\"")
print("I am studying.\nStudying python from program.")
print(r"I am studying.\nStudying python from program.")
print("--------------------------------------------------")

first_name = "Nunik "
last_name = "Nurhayati"
full_name = first_name + last_name

print(full_name)
print(first_name*3)
print(full_name[0])
print(full_name[-2])
print(full_name[6])
print(full_name[9]) #h=ke9
print(full_name[6:9]) #keenam sampai kedelapan
print(full_name[:9]) #dari awal sampai ke8
print(full_name[6:]) #dari ke6 sampai akhir
print(full_name[:]) #semua

"To know how many characters are inside."
print(len(full_name))
print("--------------------------------------------------")

"Numbers"
players = [17, 99, 83, 60, 59]
print(players)
print(players[3])

players.append(110) #dot means do something to players and append means add something on
print(players)
print(players[:2]) #yg kedua is not inccluded
players[:2] = [0, 0] #mengganti angka
print(players)
players[:2] = [] #menghilangkan dari urutan awal sampai urutan ke1
print(players)
players[:] = [] #menghilangkan semua
print(players)

print("")
print("=========================")
print("Menit ke-33")
print("")

age = 35
if age < 21:
    print("no beer for you") #maka di print ga akan muncul krn age=35
    
age = 17
if age < 21:
    print("no beer for you")
    
print("")

name = "Lucy"

if name is "Bucky":
    print("Hey Bucky")
elif name is "Lucy":
    print("Hallo Lucy")
elif name is "Slammy":
    print("Whats up Slammy")
else:
    print("ok") #ok ga akan mucul, karena maksudnya else: itu adalah jika di loop di atas tidak mengandung variable "name"
    
name2 = "Tom D"
 
if name2 is "Bucky":
    print("Hey Bucky")
elif name2 is "Lucy":
    print("Hallo Lucy")
elif name2 is "Slammy":
    print("Whats up Slammy")
else:
    print("please sign up the site")


print("")
print("=============")
print("For Loop")
print("-------------")

foods = ['ayam', 'tuna', 'kentang', 'sosis', 'daging'] 
for f in foods: #loop
    print(f) #code
    print(len(f))
    
for f in foods[:2]:
    print(f)
    print(len(f))
    
print("")
print("making range")
print("------------")

for x in range(10):
    print(x)
    
for x in range(10):
    print("Nunik is awesome")
    
for x in range(5, 12):
    print(x)
    
print("---------------")
for x in range(10, 40, 5): #10 sampe 40 @erkelipatan 5
    print(x)
    
print("")
print("while loop")
print("-----------")
    
nunik = 5
while nunik < 10:
    print(nunik)
    nunik += 1 #kalo tanpa nunik +=1 maka akan muncul 5 forever (infinitive loop)

print("-----------")

magicNumber = 26

print(7, "Nunik")

for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number.")
print("-----------")
for n in range(101):
    if n is magicNumber:
        print(n, " is the magic number.")
        break #sto@p the loop, sehingga 27 28 dst ga terprint
    else:
        print(n)
print("-----------")
numbersTaken = [2, 5, 12, 13, 17]

print("Here are the numbers that are still available:")
#menit 1.16.32
for n in range(1, 20):
    if n in numbersTaken:
        continue
    print(n)
print("-----------")

print("function")

def beef():
    print("Dayum, fuction are cool.")
    
beef() #tanpa ini, maka print ga akan muncul
beef()
beef()

def beef():
    print("Dayum, fuction are cool.")
    
def bitcoin_to_usd(btc):
    amount = btc * 527
    print(amount)

beef() #hasilnya Dayum, fuction are cool.
bitcoin_to_usd(3.85) #hasilnya 2028.95
bitcoin_to_usd(13)
print("-----------")
print("calculation")
print("")

def allowed_dating_age(my_age):
    girls_age = my_age/2. + 7 #ditambahin dot biar hasilnya desimal (20.5)
    return girls_age
buckys_limit = allowed_dating_age(27)
creepys_limit = allowed_dating_age(49)
print(buckys_limit)
print("Bucky can date girls", buckys_limit, "or older")
print("Creepy can date girls", creepys_limit, "or older")
print("-----------")




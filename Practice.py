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
    

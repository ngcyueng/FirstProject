#
#Example file for working with loops
#
x=0
#define a while loop
while (x <4):
	print (x)
	x = x+1

print("-- Define a for loop --- ")
for x in range(2,7):
		print(x)

		# use a for loop over a collection
		Months = ["Jan", "Feb", "Mar", "April", "May", "June"]
		for m in Months:
			print(m)

print("-- Pzuse the break and continue statements --")
for x in range (10,20):
			if (x == 15): break
			#if (x % 2 == 0) : continue
			print(x)

print("-- Pzuse the break statement in  LST --")
my_list = ['Siya', 'Tiya', 'Guru', 'Daksh', 'Riya', 'Guru']

for i in range(len(my_list)):
	print(my_list[i])
	if my_list[i] == 'Guru':
		print('Found the name Guru')
		break
		print('After break statement')

print('Loop is Terminated')

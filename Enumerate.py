#use a for loop over a collection
Months = ["Jan","Feb","Mar","April","May","June"]
for i, m in enumerate (Months):
		print(i,m)

		str1 = "Hello World"
		str_count1 = str1.count('o')  # counting the character “o” in the givenstring
		print("The count of 'o' is", str_count1)

		str_count2 = str1.count('o', 0, 5)
		print("The count of 'o' usingstart/end is", str_count2)

		str1 = "Welcome to Guru99 - Free Training Tutorials and Videos for IT Courses"
		str_count1 = str1.count('to')  # counting the substring “to” in the givenstring
		print("The count of 'to' is", str_count1)



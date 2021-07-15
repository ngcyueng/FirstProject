print("variable type")
Dict = {'Tim': 18,'Charlie':12,'Tiffany':22,'Robert':25}
print("variable Type: %s" %type (Dict))

#print("Comoare function")
#Boys = {'Tim': 18,'Charlie':12,'Robert':25}
#Girls = {'Tiffany':22}
#print(cmp(Girls,Boys))

print ("--- merge dict ---")
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2 = {"firstName" : "Nick", "lastName": "Price"}
my_dict1.update(my_dict2)
print(my_dict1)

print("--- Merging dictionaries using ** method (From Python 3.5 onwards) --- ")
my_dict1 = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
my_dict2 = {"firstName" : "Nick", "lastName": "Price"}
my_dict =  {**my_dict1, **my_dict2}
print(my_dict)

print("Dictionary Membership Test")
my_dict = {"username": "XYZ", "email": "xyz@gmail.com", "location":"Mumbai"}
print("email" in my_dict)
print("location" in my_dict)
print("test" in my_dict)
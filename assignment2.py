# Question 1
print("\t Question 1")

input_string = "Python is a case sensitive language"

# finding and printing the length of string.
print("Part a")
length = len(input_string)
print(length,"\n")

# reversing and printing the input string.
print("Part b")
reverse = input_string[::-1]
print(reverse,"\n")

# slicing and printing the input string.
print("Part c")
sliced = input_string[10:26]
print(sliced,"\n")

# replacing a case sensitive with object oriented 
print("Part d")
replace_string = input_string.replace("a case sensitive", "object oriented")
print(replace_string,"\n")

# finding and printing the index of a.
print("part e")
index_a = input_string.find("a")
print(index_a,"\n")

# replacing the white spaces with nothing.
print("part f")
replace_space = input_string.replace(" ", "")
print(replace_space,"\n")

# Question 2
print("\t Question 2")

# Initializing the variables.
name = "vansh Singh"
sid = 21102107
deparment_name = "Civil"
cgpa = 9.9

# string formating using format function.
print("Hey,{} Here! \nMY SID is {} \nI am form {} department and my CGPA is {} \n".format(name,sid,deparment_name,cgpa))

# Question 3
print("\t Question 3")

a = 56
b = 10

# preforming some bitwise operations and printing results.
print("The valus of a&b is ",a&b)
print("The valus of a|b is ",a|b)
print("The valus of a^b is ",a^b)
print("The value after left shift of a and b by 2 bits is ", a<<2, " and ", b<<2, "respectively")
print("The value after right shift of a by 2 bits and b with 4 bits is ", a>>2, " and ", b>>4, "respectively \n")

# Question 4 
print("\t Question 4")

# Asking for a string.
string_to_check = input("Enter the string: ")

# checking and printing the result whether the name word is present in input string or not.
if "name" in string_to_check:
    print("\nYes\n")
else:
    print("\nNo\n")

# Question 5
print("\t Question 5")

# Asking for three sides of the triangle.
side_1 = int(input("Enter the length of first side: "))
side_2 = int(input("Enter the length of second side: "))
side_3 = int(input("Enter the length of third side: "))

# Checking whether the triangle is possible or not with sides entered by the user.
if side_1 > side_2 + side_3:
    print("\nNo")
elif side_2 > side_1 + side_3:
    print("\nNo")
elif side_3 > side_1 + side_2:
    print("\nNo")
else:
    print("\nYes")

# Question 6

# Function to return the count of bits
# to be flipped to convert a to b
def countBits(a, b):

	# To store the required count
	count = 0

	# Loop until both of them become zero
	while (a or b):

		# Store the last bits in a
		# as well as b
		last_bit_a = a & 1
		last_bit_b = b & 1

		# If the current bit is not same
		# in both the integers
		if (last_bit_a != last_bit_b):
			count += 1

		# Right shift both the integers by 1
		a = a >> 1
		b = b >> 1

	# Return the count
	return count

# Driver code
a = 10
b = 7

print(countBits(a, b))

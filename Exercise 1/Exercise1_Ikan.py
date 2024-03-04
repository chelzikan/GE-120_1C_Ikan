"""

Exercise #1

"""

# Hello! For this exercise, we want to make codes that can convert decimal degrees to degree-minute-seconds and vice versa. 


print ("PART A")

# For Part A, we want our decimal value to appear as DMS. We pick our value to be 127.388758

Value = 127.388758

# Then, we split the value into its corresponding degree, minute, and second value. We'll use the 'int' fcn as it allows us to truncate the fractional part.

degree = int (Value)

minute = (Value - int(Value)) * 60

second = (minute - int(minute)) * 60

# We now have our separate DMS values. Now, we just have to put it together and separate it by -.

print ("127.388758 in DMS is {}-{}-{}".format(degree,int(minute),round(second,2)))


###


print ("PART B")

# Now, let us convert our value in DMS to decimal. We should note that our value must be a string so we can split it into separate values.

DMS = "127-23-19.53"

dms = DMS.split("-")

# The indexing in Python always starts from zero. This means that the degree part is the element 0. 

deg = int (dms [0])
min = (int (dms [1])) / 60
sec = (float (dms [2])) / 3600

# For the final step, we just have to add everything up. 

DecimalVal = deg + min + sec

print ("127-23-19.53 in Decimal is", round (DecimalVal,6))


# That's all for this exercise. Thank you!


                       

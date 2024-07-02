print("hellos")

# here are the comment i have defined

s = 3

a,b,c=1,2,3
print(a)

#concat string and number
print("{} {}".format("Value is:",b));

#find type
print(type(10))
print(type("string"))
print(type(1.23444))
print(type(1234442.34567890))
print(type(100+3j))

#list
value=[1,2,"sri",1.233,103j]
print(value)
print(value[0])
print(value[-2])
print(value[-1:-3])
value.insert(1,"ram");
value.append("end")
value[0]="updated"
del value[0]
print(value)

#tuple
val=(1,2,3,"ram",1.334,103j)
print(val[0])
# val[2]="9"
# print(val)
# val.append("44")
# del val[3]
print(val)

#dictionay
dic={"a":2,"b":"ram"}
print(dic["a"])
dic["firstname"]="sriram"
dic["firstname"]="ram"
print(dic)
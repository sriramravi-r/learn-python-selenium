ItemsInCart=0
#2 items will add to cart
# if ItemsInCart != 2: #raise Exception("prouct cart count not match") #raise exception
    #pass

# assert(ItemsInCart == 2) #throws assertion error if condition is not met

#try catch machanisms
try:
    with open("test.txt","r") as filereader:
        filereader.read()
except Exception as e:
    #raise Exception("file not found")
    #print("file not found")
    print(e)
finally:
    print("my name is finally will print if try block fail or pass")

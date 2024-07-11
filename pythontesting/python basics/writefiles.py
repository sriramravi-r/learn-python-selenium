with open("test.txt","r") as reader:
    content=reader.readlines()
    with open("test.txt","w") as writer:
        for i in reversed(content):
            writer.write(i)
    with open("test.txt","r") as read:
        for s in read.readlines():
            print(s)

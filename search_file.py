file = open("mailbox.txt", "r") 
for num, line in enumerate(file,1):
    if "WARNING" in line: 
        print("Line " + str(num) + " [found keyword]:", line)
file.close()

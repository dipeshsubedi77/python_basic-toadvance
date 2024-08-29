f = open("file.txt","r")
t = f.read()
if "twinkle" in t:
    print("twinkle is present")
else: 
    print("there is no twinkle")
def newstr(str):
    if(len(str)>3)and(str[:2]=="Is"):
        return str
    return "Is"+str
    

print(newstr("code"))
print(newstr("Isready"))

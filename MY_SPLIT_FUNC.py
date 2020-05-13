## Custom Split method ##

def mysplit(strng):
    op_ls = []
    word = ""
    if strng.isspace() or not strng:
        return op_ls
    for c in strng:
        if not c.isspace():
            word += c
        elif word:
            op_ls.append(word)
            word = ""
            
    if word:
        op_ls.append(word)
        
    return op_ls
    
    
###################################################################
a = mysplit("To be or not to be, that is the question")
b = mysplit("To be or not to be,that is the question")
c = mysplit("   ")
d = mysplit(" abc ")
e = mysplit("")


print(a) 
print(b) 
print(c) 
print(d) 
print(e)

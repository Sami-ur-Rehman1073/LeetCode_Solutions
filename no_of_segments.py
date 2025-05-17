def countSegments(s):
    result = []
    string = ""
    for i in s:
        if i == " ":
            if string != "":
              result.append(string)
            string = ""  
        else:
            string += i    
    if string != "":
        result.append(string)   
    return len(result) 
      

print(countSegments("Hello, my name is John"))

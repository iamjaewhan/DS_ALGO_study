S = input()

is_tag = 0
word = ""


for ch in S:
    if is_tag:
        if ch == ">":
            is_tag = 0
        print(ch, end='')
        continue
    else:
        if ch == "<":
            if word:
                print(word[::-1], end='')
                word = ""
            print("<", end = "")
            is_tag = 1
            
        
        elif ch == " ":
            print(word[::-1], end =' ')
            word = ""
        
        else:
            word += ch
if word:
    print(word[::-1])
            
    
        
        
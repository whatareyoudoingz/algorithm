import sys
while True: 
    stack=[]
    sentence=sys.stdin.readline( ).rstrip()
    if sentence[-1]=='.': 
        if len(sentence)==1:
            break
        sentence=sentence[:-1]
    else:
        print("no")
        break

    dic={')' : '(', ']' : '['}
    i=0
    while i < len(sentence): 
        if sentence[i] in dic.values(): 
            stack.append(sentence[i])
        elif sentence[i] in dic.keys(): 
            if stack:
                if stack[-1] == dic[sentence[i]]: 
                    stack.pop()
                else:
                    print("no")
                    break
            else: 
                print("no") 
                break
        i+=1
    if i ==len(sentence):
        if len(stack)==0: 
            print("yes")
        else:
            print("no")
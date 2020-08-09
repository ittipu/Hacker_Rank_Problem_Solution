def swap_case(sentance):
    list=[]
    newSentance=''
    for i in sentance:
        if i.isupper():
            list.append(i.lower())
        elif i.islower():
            list.append(i.upper())
        else:
            list.append(i)
    return (newSentance.join(list))

if __name__== '__main__':
    sentance=input()
    result=swap_case(sentance)
    print(result)

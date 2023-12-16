el = 0
while el != "end":
    el = int(input("1 , 2 : " ))
    if el == 1 :
        text = input("напишіть текст:") 
    list_text = list(text)
    sort_text = sorted(list_text)
    set_text = set(sort_text)
    print(set_text)
    print("thank for use :)")
    if el == 2:
        text1 = input("напишіть текст:")
        list_text1 = list(text1)
        set_text1 = set(list_text1)
        set_text1 = sorted(list_text1)
        for I in set_text1:
            print(I)
        
        
        

    else:
        print("wrong write")
        
            
    
    
    
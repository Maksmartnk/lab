el = 0
while el != "end":
    try:
        el = int(input("1 , 2 : " ))
        if el == 1 :
            w = input("write text:")
            list_nums = list(w)
            set_text = set(list_nums)
            sort_text = sorted(set_text) 
            print(list_nums)
            print("кількість елементів", len(list_nums))
            for el in sort_text:
                print(el, "=" , sort_text.count(el))


            
    except ValueError:
        print("помилка значення")
        
        
            
    
    
    

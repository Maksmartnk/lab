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
else:
    print("sorry that dont work :(") 
    
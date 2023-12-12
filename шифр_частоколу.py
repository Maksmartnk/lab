text = input("напишіть текст:")
Key = input("напишіть ключ шифрування:")
l_text = list(text)
len = len(l_text)
code_word = ""

while Key > 0:
    el = 0
    while el <len(l_text):
        a = a + 1 
        if a % Key == 0:
            if(l_text[el] != 0):
                code_word += l_text[el]
            l_text[el] = 0
        el += 1        
    Key -= 1  
print(code_word)
    
 
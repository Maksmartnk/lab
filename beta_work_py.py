el = 0
while el != "end":
    try:
        el = int(input("1 , 2 : " ))
        if el == 1 :
            input_text = input("Введіть текст: ")

        # створюю пустий словник який буду заповнювати
            letter_count = {}

        # Перебераю кожен ключ
            for char in input_text:
                
        # пробускаю пробіли
                if char != ' ':
                
                    letter_count[char] = letter_count.get(char, 0) + 1

    # результат
            print("Кількість кожної літери у введеному тексті:")
            for letter, count in letter_count.items():
                print(f"{letter}: {count}")

        if el == 2 :
            
            
    except ValueError:
        print("помилка значення")
        
        
            
    
    
    


подвоєне_слово = input("напишіть текст:")
подвоєне_слово = ''
for el in подвоєне_слово:
    
    подвоєне_слово += літера * 2
print(подвоєне_слово)

#інший варіант програми

word = input("Введіть слово: ")
doubled_word = ''.join([letter * 2 for letter in word])
print("Результат:", doubled_word)


b = 0
while b != "нічого" :
    
    class Car:
        середня_швидкість = None
        рік_випуску = None
        споживання_палива = None
    Car1 = Car() 
    Car1.середня_швидкість = "60mph"
    Car1.рік_випуску = "2007"
    Car1.споживання_палива = "6л/100км"

b = input("що ви хочете дізнатись про автомобіль :")

 
if b == "швидкість" :
    print(Car1["середня швидкість"])
 
elif b == "середня швидкість" :
    print(Car1["середня швидкість"])
 
elif b == "дата випуску" :
    print(Car1["рік випуску"])
    
elif b == "рік випуску" :
    print(Car1["рік випуску"])
 
elif b == "росхід палива" : 
    print(Car1["споживання палива"])
elif b == "все" :
    print(Car1)
else :
    print("це уся наявна інформація")    
 
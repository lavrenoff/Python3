#Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

list=[2, 3, 5, 6]
res=[]

 
if(len(list)%2==0):            
    for i in range(0,int(len(list)/2)):
        res.append(list[i]*list[len(list)-1-i])
else:    
    cnt=0
    for i in range(0,int((len(list)-1)/2)):        
        res.append(list[i]*list[len(list)-1-i])
        cnt+=1

    res.append(list[cnt]*list[cnt])    

print(res)





       

    
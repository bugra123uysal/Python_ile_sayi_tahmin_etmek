
import random


def thm():
    tahinlerim=0

    rndd=random.randint(1, 100)

    tt=False
  
    while not tt:
        
        tahinlerim +=1


       
        
        kullanıcı_sayısı=int(input("tahmin:"))

        if kullanıcı_sayısı > rndd:
            print("daha küçük sayı yazınınz")

    
    
        elif kullanıcı_sayısı < rndd:
            print("daha büyük sayı yazınınz")
            



        else:
            tt=True
            print("doğru bildiniz")    
            print(tahinlerim)






thm()    
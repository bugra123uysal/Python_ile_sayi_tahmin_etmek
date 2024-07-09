
import random


def thm():
    
    rndd=random.randint(1, 100)

    tt=False

    while not tt:
        kullanıcı_sayısı=int(input("tahmin:"))

        if kullanıcı_sayısı > rndd:
            print("daha küçük sayı yazınınz")

    
    
        elif kullanıcı_sayısı < rndd:
            print("daha büyük sayı yazınınz")



        else:

            tt=True
            print("doğru bildiniz")    






thm()    
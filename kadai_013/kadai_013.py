#ランダムの場合
import random
def calculate_total(price,tax_rate):
    totla_price=price*tax_rate
    return totla_price
print(calculate_total(random.randint(100,1000),1.1))

#1000円の場合
def calculate_total(price,tax_rate):
    totla_price=price*tax_rate
    return totla_price
print(calculate_total(1000,1.1))

#2回目
#import random

#def calculate_total(price):
    #includetax_price=price*1.1
    #return price
#price=random.randint(100,1000)
#print(price)


#以下は提出一回目の内容
#import random

#price = random.randint(100,1000)
#print (f"税抜き{price}円")

#def calculate_total(price,tax):
    #total=price+tax
    #print(f"税込み{total}円")




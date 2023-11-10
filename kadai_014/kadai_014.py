#元のコード
#price1 = 100
#price2 = 200

#def total():
    #tax = 1.1
    #return price1 + price2

#print (total() * tax)

#修正後
price1 = 100
price2 = 200
totla_price1=price1+price2

def total(totla_price1,tax):
    total_price2=totla_price1*tax
    return total_price2

print (total(totla_price1,1.1))


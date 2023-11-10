#金額は100~1000円でランダムに決定
#税抜き金額を最初に表示

import random

price = random.randint(100,1000)
print (f"税抜き{price}円")

def calculate_total(price,tax):
    total=price+tax
    print(f"税込み{total}円")

calculate_total(price,tax=price*0.1)
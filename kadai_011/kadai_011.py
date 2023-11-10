#listは変数のためlist_1に変更
#内容：リストの中身を全て取り出して、for、while、それぞれを利用して記述
list_1 = ["水","金","地","火","木","土","天","海","冥"]

#for文
for planet in list_1:
        print( planet )

#while文
planet = 0
while planet <= 8:
    print( list_1[planet] )
    planet = planet + 1



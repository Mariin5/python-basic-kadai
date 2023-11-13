print("==================")

#時間表示
import time
print(time.strftime("%Y年%m月%d日%H時%M分%S秒",time.localtime()))

#年齢は100歳までの5の倍数をランダムで選定
import random
for age in range(0,50):
    personal_data={"name":"Marina", "age":random.randint(0,20)*5}
    personal_data_2={"name":"Marina_2", "age":random.randint(0,20)*5}
    personal_data_3={"name":"Marina_3", "age":random.randint(0,20)*5}

#1人目
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def check_adult(self):
        if 20 <= self.age :
            print(f"{self.name}は{self.age}歳なので大人です")
        else :
            print(f"{self.name}は{self.age}歳なので大人ではありません") 
human = Human(personal_data["name"], personal_data["age"])
human.check_adult()


#2人目
class Human_2(Human):
    def check_adult(self):
        if 20 <= self.age :
            print(f"{self.name}は{self.age}歳なので大人です")
        else :
            print(f"{self.name}は{self.age}歳なので大人ではありません") 
Human_2 = Human_2('Marina_2',random.randint(0,20)*5 )
Human_2.check_adult()


#3人目
class Human_3(Human):
    def check_adult(self):
        if 20 <= self.age :
            print(f"{self.name}は{self.age}歳なので大人です")
        else :
            print(f"{self.name}は{self.age}歳なので大人ではありません") 
Human_3 = Human_3('Marina_3',random.randint(0,20)*5 )
Human_3.check_adult()

print("==================")
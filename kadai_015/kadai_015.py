'''
名前(name)と年齢(age)の属性を持つHumanクラスを作成してください。
nameとageを標準出力(print)するメソッド(printinfo)を追加してください。

Humanクラスのインスタンスは、変数に代入してプログラム内で使用してください。
'''

class Human:
    def __init__(self):
        self.name=""
        self.age=""
    def printinfo(self,name,age):
      self.name = name
      self.age = age
    def show_printinfo(self):
       print(self.name)
       print(self.age)
person=Human()
person.printinfo("Marina",31)
person.show_printinfo ()  

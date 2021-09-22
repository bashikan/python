# class Member:
#     '''スポーツクラブの会員クラス'''
#     def __init__(self,no:int,name:str,weight:float) -> None:
#         #コントラクタ
#         self.no=no #会員番号
#         self.name=name  #指名
#         self.weight=weight  #体重

#     def print(self)->None:
#         #データの表示
#         print(('{}:{} {}kg'.format(self.no,self.name,self.weight)))
# #会員クラスのテスト

# yamada=Member(15,'山田太郎',72.7)
# sekine=Member(37,'関根信彦',65.3)

# yamada.print()
# sekine.print()


#11-1
# import math
# class Circl:
#     PI=3.1415
#     def circlk(self,r):
#         sum=r*r*Circl.PI
#         return math.floor(sum*10**3)/(10**3)

#     def circlk2(self,r):
#         syu=(r+r)*Circl.PI
#         return math.floor(syu*10**3)/(10**3)

# circl=Circl()
# r=int(input('半径を整数値で入力:'))
# ck=circl.circlk(r)
# sk=circl.circlk2(r)
# print('円周は{}です'.format(sk))
# print('円の面積は{}です'.format(ck))

#11-2

class goukei:
    def keisan(self,x,y):
        self.x=x
        self.y=y
        sum=0
        for i in range(self.x,self.y+1):
            sum+=i
        return sum
keisan=goukei()
x=int(input('整数を入力してください:'))
y=int(input('一つ目の値より大きい値を入力してください:'))
keisank=keisan.keisan(x,y)
print('{}から{}までの合計値は{}'.format(x,y,keisank))
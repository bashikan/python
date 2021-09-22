# n=int(input('整数値:'))
# if n>0:
#     print('その値は正です')
# else :
#     print('その値は0か不です')

#4-1
# n=int(input('0から100までの数値を入力してください'))
# if n>=80:
#     print('合格です')

#4-5
# n=int(input('0から100までの数値を入力してください'))
# if n>=60:
#      print('合格です')
# else:
#     print('不合格です')

#4-2
# print('0から100までの得点を2つ入力してください')
# x=int(input('国語の得点:'))
# y=int(input('英語の得点:'))
# if x==100 and y==100:
#      print('合格です')

#4-3     
# print('0から100までの得点を2つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# if x>=80 and y>=80:
#      print('二科目とも合格です')

#4-4
# print('0から100までの得点を2つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# if x>=80 or y>=80:
#      print('合格です')

#4-6
# n=int(input('整数値を入力してください'))
# if n%2==0:
#      print('偶数です')
# elif n%2==1:
#     print('奇数です')

#4-7
# print('文字を２つ入力してください')
# x=input('一つ目の文字:')
# y=input('二つ目の文字:')
# if x==y:
#     print('同じ文字です')
# else:
#     print('異なる文字です')

#4-8
# print('0~100までの得点を２つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# if x>=60 and y>=60:
#      print('合格です')
# else:
#      print('不合格です')

#4-9
# print('0~100までの得点を２つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# if x>=80 or y>=80:
#      print('合格です')
# else:
#      print('不合格です')

#4-10
# n=int(input('0~100までの得点を入力してください:'))
# if n>100 or n<0:
#     print('入力値が不正です')
# else:
#     print('正しい入力値です')

#4-11
# print('0~100までの得点を２つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# if x>=70 and y>=70:
#         print('合格')
# else:
#     print('不合格')

#4-12
# n=int(input('四桁の西暦を入力してください:'))
# if n%4==0:
#     if n%100==0:
#         if n%400==0:
#             print('閏年です')
#         else:
#             print('平年です')
#     else:
#         print('閏年です')
# else:
#     print('平年です')
        
#4-13
# n=int(input('0~100の得点を入力してください'))
# if n==100:
#     print('満点合格です')
# elif n<100 and n>=60:
#     print('合格です')
# elif n<60:
#     print('不合格です')

#4-14
# n=int(input('0~100の得点を入力してください'))
# if n>100 or n<0:
#     print('入力値が不正です')
# elif n==100:
#     print('満点合格です')
# elif n<100 and n>=60:
#     print('合格です')
# elif n<60:
#     print('不合格です')

#4-15
# print('0~100までの値を２つ入力してください')
# x=int(input('一つ目の値:'))
# y=int(input('二つ目の値:'))
# if x==y:
#     print('同じ値です')
# elif x>y:
#     print('値が大きいのは{}です'.format(x))
# elif y>x:
#     print('値が大きいのは{}です'.format(y))

#4-16
# print('整数値を３つ入力してください')
# x=int(input('一つ目の整数値:'))
# y=int(input('二つ目の整数値:'))
# z=int(input('三つ目の整数値:'))
# i=max(x,y,z)
# if x==y==z:
#     print('同じ値です')
# else:
#     print('最大値は{}'.format(i))

#4-17
# print('0~100までの得点を２つ入力してください')
# x=int(input('一つ目の得点:'))
# y=int(input('二つ目の得点:'))
# x,y=sorted([x,y])
# print('{},{}'.format(y,x))

#4-18
x=int(input('0~100までの国語の得点を入力してください'))
if x>=80:
    y=int(input('0~100までの英語の得点を入力してください'))
    if y>=80:
        print('合格です')
    else:
        print('不合格です')
else:
    z=int(input('0~100までの数学の得点を入力してください'))
    if z>=80:
        print('合格です')
    else:
        print('不合格です')

# n=int(input('正の整数値:'))
# if n>0:
#     if n%2==0:
#         print('その値は正の偶数です。')
#     else:
#         print('その値は正の奇数です。')
# else:
#     print('正ではない値が入力されました。')
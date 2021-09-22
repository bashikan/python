#8-1
# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in range(len(lst)):
#     print('list[',i,']=',lst[i],sep='')

#8-2
# lst=['茨城県','栃木県','群馬県','千葉県','東京都','埼玉県','神奈川県']
# for i in range(len(lst)):
#     print(lst[i])

#8-3
# gu=[]
# ki=[]
# for i in range(10):
#     kac=int(input('{}件目:整数を入力='.format(i+1)))
#     if kac %2==0:
#         gu.append(kac)
#     else:
#         ki.append(kac)
# print('偶数値配列=[',gu,']',sep='')
# print('奇数値配列=[',ki,']',sep='')

#8-14
# yasai={
#     '野菜':'季節',
#     'キャベツ':'春',
#     'スイカ':'夏',
#     'ナス':'秋',
#     'ハクサイ':'冬'
# }
# for key,value in yasai.items():
#     print(key,':',value,sep='')

#8-15
# yasai={
#     '野菜':'季節',
#     'キャベツ':'春',
#     'スイカ':'夏',
#     'ナス':'秋',
#     'ハクサイ':'冬'
# }
# for key,value in yasai.items():
#     if value=='季節' or value=='春':
#         print(key,':',value,sep='')

#8-16
# hoo={
#     'id':100,
#     'name':'大原太郎',
#     'age':19,
# }
# hoo['age']=20
# for key,value in hoo.items():
#     print(key,':',value,sep='')

#8-17
kamok=list({
    '国語',75,
    '数学',80,
    '理科',65,
    '社会',90,
    '英語',70,
}.items())

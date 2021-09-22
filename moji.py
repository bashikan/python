# moji='abc'+'def'
# print(moji)

# moji='-'*10
# print(moji)

#14-1
# moji=input('文字列を入力:')
# print(moji)

#14-2
# moji=input('文字列を入力:')
# print(len(moji))

#14-3
# moji=input('文字列を入力:')
# mojik=len(moji)
# if mojik>10:
#     for i in range(10):
#         print('{}'.format(moji),end='')
# else:
#     print(moji)

#14-4
# print('文字列を二つ入力してください')
# moji1=input('一つ目の文字列を入力:')
# moji2=input('二つ目の文字列を入力:')
# if moji1==moji2:
#     print('同じ文字列です')
# else:
#     print('違う文字列です')

#14-5
# moji1='東京都千代田区'
# moji2='神田神保町'
# print(moji1)
# print(moji2)
# print(moji1+moji2)

#14-6
# moji1='東京都神田神保町'
# moji2='千代田区'
# print(moji1)
# print(moji2)
# print(moji1[0:2],moji2,moji1[3:],sep='')

#14-7
# moji='東京都千代田区神田神保町'
# print(moji)
# print(moji[3:])

#14-8
# moji='東京都千代田区神田神保町'
# print(moji)
# print(moji[3:7])

#14-9
# moji='東京都千代田区神田神保町千代田ビル１階'
# print(moji)
# cmoji=(moji.replace('千代田','中央'))
# print(cmoji)
# ct=cmoji.count('中央')
# print('置換した個数は{}です'.format(ct))

#14-10
# moji='東京都千代田区神田神保町'
# print(moji)
# sk='田'
# for i in range(len(sk)):
#     moji=moji.replace(sk[i],'')
# print(moji)

#14-11
# jyus=input('住所を入力してください:')
# srt=jyus.count('市')
# srt2=jyus.count('郡')
# if srt==1:
#     jyus+='市'
#     print(jyus)
# elif srt2==1:
#     jyus+='群'
#     print(jyus)
# else:
#     jyus+='東京２３区'
#     print(jyus)

#14-12
jyus=input('住所を入力してください:')
target='都'
target2='道'
target3='府'
target4='県'
ct=jyus.count('都')
ct2=jyus.count('道')
ct3=jyus.count('府')
ct4=jyus.count('県')
srt=jyus.find(target)
srt2=jyus.find(target2)
srt3=jyus.find(target3)
srt4=jyus.find(target4)
kjyus=jyus[srt+1:]
kjyus2=jyus[srt2+1:]
kjyus3=jyus[srt3+1:]
kjyus4=jyus[srt4+1:]
if ct==1:
    print(kjyus)
elif ct2==1:
    print(kjyus2)
elif ct3==1:
    print(kjyus3)
elif ct4==1:
    print(kjyus4)
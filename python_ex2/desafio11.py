from time import sleep
import emoji

print('\033[35mContagem regressiva para os fogos de artifícios!!')
for c in range(10 , -1, -1):
    sleep(1)
    print(c)
print(emoji.emojize('\033[41mBOMM!:sparkler::sparkles:\033[m')*25 )
print('              \033[34;43mFeliz ano novo!!\033[m'*3)
print(emoji.emojize('\033[46mBOMM!:sparkler::sparkles:\033[m')*25 )

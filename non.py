from random import choice
s='zhengyiru nihaotianqi,zhenbucuo'
for i in range (32):
    a=choice(s)
    if ' '==a:
	    print('yes great')
    elif ','==a:
	    print('ok well')
    else :
	    print(a,'nono')

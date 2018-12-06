# ==2.
for i in range(0,1000):
    


# ==3. Algo
str1 ='abcd'
str2 ='abdbacade'

for i in str2:
    if str1.find(i) < 0:
        print (f"{i} is the extra letter." )
    else:
        print('all letter matched.')
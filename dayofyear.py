def dayOfProgrammer(y):
    if (y==1918):
        return '26.09.1918'
    elif((y<= 1917)&(y%4 == 0))or((y>1918)&(y%400==0 or((y%4==0) and (y%100!= 0)))):
        return '12.09.%s' %y
    else:
        return '13.09.%s' %y

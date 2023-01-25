def minimo_comun_multiplo(num1,num2):
    i, a, stop=1,1,False
    while(stop==False):
        if (num1*i==num2*a):
            stop=True
        elif (num1*i>num2*a):
            a+=1
        elif (num1*i<num2*a):
            i+=1
    return num1*i


def maximo_comun_divisor(num1,num2):
    if(num1>num2):
        limit=num2
    elif(num2>num1):
        limit=num1
    else:
        limit=num1
    stop=False
    while(limit>1 and stop==False):
        if(num1%limit==0 and num2%limit==0):
            stop=True
        else:
            limit-=1
    return limit
print(maximo_comun_divisor(24,36))
print(minimo_comun_multiplo(24,36))
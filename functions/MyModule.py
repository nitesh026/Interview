zero_nine = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']
ten_nineteen=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
twenty_hundred= ['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninty']
thousand = ['','hundred','thousand','lack']
def average(n1,n2):
    return (n1+n2)/2

def sum(n1,n2):
    return n1+n2

def big_number(n1,n2):
    if n1>n2:
        print(n1, ': is big number')
    elif n1==n2:
        print(n1,'=',n1)
    else:
        print(n2, 'is big number')

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact = fact*i
    return fact


def number_to_words(number):
    return converted_word(list_number(number))

def list_number(number):
    list_num = []
    while number >0:
        list_num.append(int(number%10))
        number = int(number/10)
    return list_num

def converted_word(list_num):
    count = len(list_num)-1
    print(count)
    print(list_num)
    if count ==3:
        return str(zero_nine[list_num[3]]) + ' ' + thousand[2] + ' ' +str(zero_nine[list_num[2]]) +' '+thousand[1]+' '+twenty_hundred[list_num[1]-1]+' '+zero_nine[list_num[0]]
    elif count==2:
        return str(zero_nine[list_num[2]])+' '+thousand[1]+' '+twenty_hundred[list_num[1]-1]+' '+zero_nine[list_num[0]]
    elif count==1:
        return twenty_hundred[list_num[1]-1] +' '+zero_nine[list_num[0]]
    elif count==0:
        return zero_nine[list_num[0]]












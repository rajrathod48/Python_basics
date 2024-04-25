print("raj rathod")
def calc_sum(x,y):
    return(x+y)
calc_sum(5,8)

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)
    return avg

calc_avg(5,5,5)     

cities = ["bhavnagar", "surat","baroda"]
states= ["gujrat","goa","delhi","punjab"]

def print_len(list):
    print(len(list))

print_len(cities)
print_len(states)

print(cities[0],end=" ")
print(cities[1])

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(cities)

def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)

number = int(input("enter a number :  "))

if number > 0:
    print("number is poositive")


  
  
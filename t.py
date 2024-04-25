def calc_fact(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(fact)
calc_fact(5)

def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val,"usd =",inr_val,"INR")

converter(89)




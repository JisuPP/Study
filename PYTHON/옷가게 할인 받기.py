def solution(price):
    if price >= 500000:
        return int(price*0.8)
    elif price >= 300000:
        return int(price*0.9)
    elif price >= 100000:
        return int(price*0.95)
    else:
        return price
    
#################################
    
def solution(price):
    discount_rate = {500000 : 0.8, 300000 : 0.9, 100000 : 0.95, 0 : 1}
    for discount_price, discount_rate in discount_rate.items():
        if price >= discount_price:
            return int(price*discount_rate)
        
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000] if k<=price]*5)*price//100)


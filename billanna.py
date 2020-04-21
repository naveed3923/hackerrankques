def bonAppetit(bill, k, b):
    total=sum(bill)
    actual=total-bill[k]
    anna=actual/2
    diff=b-anna
    if diff>0:
        print(int(diff))
    else:
        print('Bon Appetit')

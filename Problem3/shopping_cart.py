carts =[]

carts.append({'목록':'사과','가격' : 1000,'개수':2})
carts.append({'목록':'바나나','가격' : 800,'개수': 3})
carts.append({'목록':'오렌지','가격' : 1500,'개수': 1})


print('쇼핑 카트:')

for cart in carts :
    print(f'{cart['목록']}: {cart['개수']}개 (개당 {cart['가격']}원) = {cart['개수']*cart['가격']}원')

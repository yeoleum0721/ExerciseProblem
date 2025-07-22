price = int(input('상품 가격을 입력하세요 : '))
discount = int(input('할인율을 입력하세요(%) : '))

print(f'원래 가격 : {price}원')
print(f'할인율 : {discount}')


print(f'할인금액 : {price *(discount/100)}원')
print(f'할인금액 : {price - price *(discount/100)}원')

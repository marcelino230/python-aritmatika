f = float(input('masukan suhu dalam fahrenheit :'))
k = (f-32)*5/9+237.15
print('suhu dalam kelvin =', k, "kelvin")

ke = float(input("masukan suhu dalam kelvin :"))
fa = (9/5)*(ke-237.15)+32
print("suhu dalam fahreinheit =", fa, "fahrenheits")

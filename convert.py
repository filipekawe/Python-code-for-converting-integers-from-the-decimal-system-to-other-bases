#Python code for converting integers from the decimal system to other bases
value=int(input("type the value in decimal system: "))
base=int(input("type the base that you whant to convert: "))
quotient=abs(value)
remains=""
while quotient > 0:
    remains+=str(quotient%base)
    quotient=quotient//base
if (value > 0):
    print("({})10 = ({}) {}".format(value, remains[::-1], base))
else:
    print("({})10 = (-{}) {}".format(value, remains[::-1], base))




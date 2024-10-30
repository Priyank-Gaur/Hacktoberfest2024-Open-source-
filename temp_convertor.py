def temp_converter(is_farenheit):
    if is_farenheit==1:
        x=(t-32)*5/9
        return round(x,4)
    elif is_farenheit==0:
        x=(t*9/5)+32
        return round(x,4)
is_farenheit=int(input())
t=float(input())
print(temp_converter(is_farenheit))

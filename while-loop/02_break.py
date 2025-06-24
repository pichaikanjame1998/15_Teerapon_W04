numbers = [12,15,63,21,24,30]
divisor = 6

print(f"ตัวที่หาร {divisor} ลงตัว :")

for i in numbers:
    if i % divisor == 0:
        print(f"{i} หาร {divisor} ลงตัว")
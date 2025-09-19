# 18
def temperature(tmp):
  if tmp > 0 and tmp < 100:
    return "Agregatno stanje je tečno"
  elif tmp < 0:
    return "Agregatno stanje je čvrsto"
  else:
    return "Agregatno stanje je gasovito"

print(temperature(112))


#23
import math

def is_part_of(x, y):
    distance = math.sqrt(x**2 + y**2)

    if distance >= 4 and distance <= 6:
        if x - y - 4 >= 0:
            print("Pripada")
        else:
            print("Ne pripada")
    else:
        print("Ne pripada")

is_part_of(5, 5)
is_part_of(5, 0)
is_part_of(3, 3) 
is_part_of(4, 0)

# 39

def is_narcissistic(num):

    digits = str(num)
    length = len(digits)

    total = sum(int(el)**length for el in digits)
    
    return total == num

print(is_narcissistic(153))
print(is_narcissistic(9474))
print(is_narcissistic(123))

# 96
def split_string(text, number):
    result = []
    i = 0 
    while i < len(text):
        chunk = text[i:i + number]

        if len(chunk) < number:
            missing = number - len(chunk)
            chunk = chunk + ("*" * missing)

        result.append(chunk)
        i += number

    return result


print(split_string("danas polazemo test", 5))
print(split_string("kurs web program.", 6))
print(split_string("da", 7))     
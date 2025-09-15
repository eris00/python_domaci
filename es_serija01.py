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


# 96

"""

def break_str (str, num):
  res = []
  for i in range(0, len(str), num):
    substr = str[i+n]
"""

# 39

def is_narcissistic(num):

    digits = str(num)
    length = len(digits)

    total = sum(int(el)**length for el in digits)
    
    return total == num

print(is_narcissistic(153))
print(is_narcissistic(9474))
print(is_narcissistic(123))
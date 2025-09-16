"""
1. Napisati program koji racuna površinu i obim pravougaonika.
"""

'''
def count_rectangle(rec):
  res = dict()
  width = rec["width"]
  height = rec["height"]

  area = height * width
  perimeter = 2*height + 2*width

  res["area"] = area
  res["perimeter"] = perimeter
  return res

rectangle = {"width": 7, "height": 4}
res = count_rectangle(rectangle)
print(res)
'''


"""
3. Napisati program koji racuna razliku kvadrata.
"""
''' 
def diff_of_squares(squares):
  a = squares[0]
  b = squares[1]

  diff = a**2 - b**2

  return diff

square = (7,4)
res = diff_of_squares(square)
print(res)

'''


"""
12. Kreirati algoritam koji računa koje godine je rođen Miloš ukoliko je poznato da danas ima
N godina.

"""
'''
from datetime import date
def birth_year(age):
  today = date.today().year
  year = today - age
  return year

res = birth_year(74)
print(res)
'''


"""
16. Ako je cijena taksija za jedan kilometar 0.5e, a početna cijena je 1e, napisati kod koji za
unijeti broj pređenih kilometara računa cijenu vožnje.
"""
'''
def taxi_price(kilometers, price_per_km=0.5, start_price=1):
    return start_price + price_per_km * kilometers

res = taxi_price(4.21, 2, 1)
print(res)
'''


"""
17. Knjižara "Bukvarnica" je posebno mjesto gdje svaka knjiga ima svoju priču. Kako bi
proslavili dolazak novog godišnjeg doba, knjižara je odlučila da uvede popust - svaka
knjiga dobija popust koji se može otkriti samo uz pomoć programa. Kao pomoćnik u
knjižari, vaš zadatak je da kreirate program koji će izračunati konačnu cijenu knjige
nakon primijenjenog popusta
"""
'''
def book_discount(discount, price):
  return price * (1- discount)

res = book_discount(0.25, 70)
print(res)
'''


"""
18. Cijena konzole za igre PlayStation 5 je prvo porasla 10%, pa je smanjena 10%. Ako je
poznata početna cijena konzole, napisati program koji određuje cijenu nakon tih
promjena
"""
'''
def ps5_price(price):
  first_price = price * (1-0.10)
  after_discount = first_price * (1-0.10)
  return after_discount

res = ps5_price(533)
print(res)
'''


"""
19. Napisati program koji za zadati trocifreni broj računa zbir cifara tog broja
"""
'''
def sum_of_three_digits(num):
  third_digit = num % 10
  second_digit = (num % 100) // 10
  first_digit = int(str(num // 10)[0])

  return first_digit + second_digit + third_digit

res = sum_of_three_digits(326)
print(res)
 '''


"""

"""
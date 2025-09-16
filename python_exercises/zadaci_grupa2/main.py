""" ** DRUGA GRUPA ZADATKA ZA VJEZBANJE ** """


"""
1. U tajanstvenom svijetu postoji portal koji se otvara samo kada mu se date paran broj.
Kao mladi čarobnjak na svom prvom zadatku, dobio si čarobni štapić koji može
generisati brojeve. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je broj koji
je čarobni štapić generisao paran. Ako jeste, algoritam treba da ispiše: "Portal se
otvara!" Ako nije, algoritam treba da ispiše: "Portal ostaje zatvoren."

"""
'''
def portal_odd_even(num):
  if num % 2 == 0:
    print("Portal se otvara")
  else:
    print("portal je zatvoren")

portal_odd_even(4)
'''


"""
2. U selu poznatom po svojim jabukama, održava se godišnje takmičenje u berbi jabuka
između i najbliži pobjedi su Petar i Miloš. Petar tvrdi da je ubrao p jabuka, dok Miloš tvrdi
da je ubrao m jabuka. Vaš zadatak je da kreirate algoritam koji će provjeriti da li je Petar
uspio da ubere više jabuka nego Miloš i shodno tome ispiše poruku o pobjedniku.
Pretpostaviti da ne mogu ubrati isti broj jabuka.

"""
'''
def apple_winer(p,m):
  if p > m:
    print("Petar je pobjednik")
  else:
    print("Miloš je pobjednik")

petar_jabuke = 7
milos_jabuke = 6
apple_winer(petar_jabuke, milos_jabuke)
'''


"""
3. Zamislimo da pravimo program koji treba da odluči da li student može da pristupi ispitu.
Postoje dva uslova: student mora imati više od 75% prisustva na predavanjima i mora
imati predate sve seminarske radove. Oba uslova moraju biti zadovoljena da bi student
mogao pristupiti ispitu. Algoritam treba da štampa odgovarajuću poruku. Dodatak:
prisustvo se unosi u procentima, a dio za seminarske radove na sledeci nacin -> 0
predstavlja da bar jedan seminarski rad nije uradjen, a 1 da su svi seminarski radovi
uradjeni.
"""
'''
def check_stud():
  full_name = input("Enter student name: ")
  attendance = input("Enter student attendance in %: ")
  is_seminar_finished = input("Is student did all seminar paper? Enter: 1 for YES, 0 for NO:  ")

  studObj = dict()

  studObj["full_name"] = full_name.strip()
  studObj["attendance"] = float(attendance.strip())
  studObj["is_seminar_finished"] = bool(int((is_seminar_finished.strip())))
  studObj["can_take_exam"] = True if studObj["attendance"] > 0.75 and studObj["is_seminar_finished"] else False

  return studObj

res = check_stud()
val = res["can_take_exam"] = f"Student {res["full_name"]} {"može" if res["can_take_exam"] else "ne može"} izaći na ispit."
print(val)
 '''

"""
4. Kućni red zabranjuje pravljenje buke prije 6 časova, između 13 i 17 časova i nakon 22
časa. Napiši program koji radnicima govori da li u nekom datom trenutku mogu da
izvode bučnije radove
"""
'''
from datetime import datetime

def can_do_noise():
  current_hour = datetime.now().hour
  if current_hour < 6 or (13 <= current_hour < 17) or current_hour >= 22:
    return("Ne može!")
  else:
    return ("Može!")

  
res = can_do_noise()
print(res)
'''

"""
7. Takmičari su radili testove iz matematike i programiranja. Za svaki predmet dobili su
određeni broj poena (cio broj od 0 do 50). Takmičari se rangiraju po ukupnom broju
poena iz oba predmeta. Ako dva takmičara imaju isti broj poena, pobjednik je onaj koji
ima više poena iz programiranja. Potrebno je napisati program koji određuje pobjednika
takmičenja
"""

def stud_winner(studs):

  best_math_stud = max(studs, key=lambda x: x["math"])
  best_programming_stud = max(studs, key=lambda x: x["programming"])
  print(best_math_stud)
  print(best_programming_stud)



students = [
  {"full_name":"Eris Sutkovic", "math":37, "programming": 47},
  {"full_name":"John Doe", "math":42, "programming": 22},
  {"full_name":"Mark Pitterson", "math":47, "programming": 46},
  {"full_name":"Derryl Smith", "math":12, "programming": 23},
  {"full_name":"Rob Kedrick", "math":47, "programming": 48},
]

stud_winner(students)


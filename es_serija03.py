"""
File: Domaci zadatak 4
"""

from functools import reduce
from datetime import datetime


# 2
def higher_than_85(names_list, grades_list, limit=8.5):
  result = []
  for name_ls, grade in zip(names_list, grades_list):
    try:
      g = float(grade)
    except (TypeError, ValueError):
      continue
    if g > limit:
      result.append((name_ls, g))
  return result

students = ["Eris", "Petar", "John", "Marq"]
averages = [9.2, 8.3, 8.7, 10]

out_list = higher_than_85(students, averages)
print(out_list)


# 5
def avg_by_subject(items):
  ok_list = list(filter(lambda item: isinstance(item, tuple) and len(item) == 3, items))

  subj_grade = list(map(lambda item: (item[2], float(item[1])), ok_list))

  sums_counts = reduce(
    lambda acc, curr: (acc.update({curr[0]: [acc.get(curr[0], [0.0,0])[0] + curr[1],acc.get(curr[0], [0.0, 0])[1] + 1]}) or acc),subj_grade,{}
  )

  avg_map = dict(map(lambda el: (el[0], el[1][0] / el[1][1] if el[1][1] else 0.0), sums_counts.items()))
  return avg_map

student_lst = [
    ("Eris", 9.0, "Physics"),
    ("Pitter", 8.5, "Hemistry"),
    ("Marq", 10, "Computer Science"),
    ("Dennis", 7.5, "Geography"),
    ("Derryl", 8.0, "Art"),
]

res = avg_by_subject(student_lst)
print(res)



# 14

def append_to_file(list_of_students):
  with open("students.txt", "a", encoding="utf-8") as f:
    for item in list_of_students:
      name = item.get("fname", "")
      surname = item.get("lname", "")
      year = item.get("year", "")
      avg = item.get("avg", "")
      line = f"{name},{surname},{year},{avg}\n"
      f.write(line)

def get_students_with_greater_grade(year, grade):
  grade_min_map = {
    "A": 9.5,
    "B": 8.5,
    "C": 7.5,
    "D": 6.5,
    "E": 6.0
  }
  letter = str(grade).upper()
  min_val = grade_min_map.get(letter, None)
  if min_val is None:
    return []

  out_list = []
  try:
    with open("students.txt", "r", encoding="utf-8") as f:
      for line in f:
        line = line.strip()
        if not line:
          continue
        parts = line.split(",")
        if len(parts) != 4:
          continue

        name, surname, year_str, avg_str = parts
        try:
          year_val = int(year_str)
          avg_val = float(avg_str)
        except ValueError as e:
          print("error occured: ", e)

        if year_val == year and avg_val >= min_val:
          out_list.append({
            "fname": name,
            "lname": surname,
            "year": year_val,
            "avg": avg_val
          })
  except FileNotFoundError as e:
    print("error occured")
    return []

  return out_list


stud_ls1 = [
  {"fname": "Eris", "lname": "Sutkovic", "year": 3, "avg": 9.2},
  {"fname": "John", "prelnamezime": "Doe", "year": 2, "avg": 6.2},
  {"fname": "Petar", "lname": "Petrovic", "year": 1, "avg": 7.4},
]
append_to_file(stud_ls1)

stud_ls2 = [
  {"fname": "Derryl", "lname": "Johnson", "year": 3, "avg": 6.1},
  {"fname": "Marcus", "lname": "Pitterson", "year": 2, "avg": 7.7},
]
append_to_file(stud_ls2)

res_1 = get_students_with_greater_grade(3, "C")
print("year=3, grade=C =>", res_1)

res_2 = get_students_with_greater_grade(1, "A")
print("year=1, grade=A =>", res_2)

# If file students.txt already exist in same directorium as this file, you need to delete them first and then run the code for task result!!

print("____  ____  ____  ____  ____  ____  ____")


# 16

ALLOWED_GENRES = [
	"Action",
	"Adventure",
	"RPG",
	"Shooter",
	"Strategy",
	"Sports",
	"Racing",
	"Puzzle",
	"Horror",
]

def is_valid_rating_text(rating_text):
	if "." not in rating_text:
		return False
	parts_list = rating_text.split(".")
	if len(parts_list) != 2:
		return False
	if len(parts_list[1]) != 2:
		return False
	try:
		rating_value = float(rating_text)
	except ValueError:
		return False
	if rating_value < 1.0 or rating_value > 10.0:
		return False
	return True

def validate_game_fields(name_text, rating_text, year_text, publisher_text, genres_text):
	if not (2 <= len(name_text) <= 50):
		return False, "Naziv mora imati 2 do 50 karaktera."
	if not is_valid_rating_text(rating_text):
		return False, "Ocjena mora biti float 1-10 sa dvije decimale (npr. 8.50)."
	try:
		year_value = int(year_text)
	except ValueError:
		return False, "Godina mora biti cijeli broj."
	curr_year = datetime.now().year
	if not (year_value > 1950 and year_value < curr_year):
		return False, f"Godina mora biti veća od 1950 i manja od {curr_year}."
	if publisher_text is not None and publisher_text != "":
		if not (2 <= len(publisher_text) <= 40):
			return False, "Izdavač (ako se unosi) mora imati 2 do 40 karaktera."
	genres_list = [g for g in genres_text.split(" ") if g.strip() != ""]
	if len(genres_list) == 0 or len(genres_list) > 3:
		return False, "Žanrovi: unijeti 1 do 3 žanra odvojena space-om."
	lower_allowed = [x.lower() for x in ALLOWED_GENRES]
	for element in genres_list:
		if element.lower() not in lower_allowed:
			return False, f"Žanr '{element}' nije dozvoljen. Dozvoljeni: {', '.join(ALLOWED_GENRES)}"
	return True, ""
def clean_and_copy_games(input_file_name="igrice.txt", output_file_name="igrice_valid.txt"):
	valid_lines = []
	curr_year = datetime.now().year
	with open(input_file_name, "r", encoding="utf-8") as file_object:
		for line_text in file_object:
			line_text = line_text.strip()
			if not line_text:
				continue

			parts_list = line_text.split(";")
			if len(parts_list) == 5:
				name_text, rating_text, year_text, publisher_text, genres_text = parts_list
			elif len(parts_list) == 4:
				name_text, rating_text, year_text, genres_text = parts_list
				publisher_text = ""
			else:
				continue

			is_ok, error_msg = validate_game_fields(name_text, rating_text, year_text, publisher_text, genres_text)
			if is_ok:
				rating_value = float(rating_text)
				line_clean = f"{name_text};{rating_value:.2f};{int(year_text)};{publisher_text};{genres_text}"
				valid_lines.append(line_clean)

	with open(output_file_name, "w", encoding="utf-8") as out_object:
		for element in valid_lines:
			out_object.write(element + "\n")

	return valid_lines

def print_lines_simple(lines_list):
	index_value = 1
	for element in lines_list:
		print(f"{index_value}. {element}")
		index_value += 1

def prompt_add_new_games(output_file_name="igrice_valid.txt"):
	print("\nDa li zelite doadti nove igrice? za DA pretisnite y za ne pretisnite 'n' na tastaturi  ")
	choice_text = input("> ").strip().lower()
	if choice_text != "y":
		return

	print("\nMozete unijeti samo ove zanrove: ", ", ".join(ALLOWED_GENRES))
	print("Ako zelite da prekinete kucajte q.\n")

	while True:
		name_text = input("Unesite naziv: ").strip()
		if name_text.lower() == "q":
			break

		rating_text = input("Ocjena: ").strip()
		year_text = input("Godina: ").strip()
		publisher_text = input("Izdavac (enter ukoliko ne zelite da unesete izdavaca): ").strip()
		genres_text = input("Zanrovi (od 1 do 3 sa space razmakom) ").strip()

		is_ok, error_msg = validate_game_fields(name_text, rating_text, year_text, publisher_text, genres_text)
		if not is_ok:
			print("Error has occured: ", error_msg)
			print("Probajte ponovo da unesete ili izadjite pretiskom na q.\n")
			continue

		rating_value = float(rating_text)
		clean_line = f"{name_text};{rating_value:.2f};{int(year_text)};{publisher_text};{genres_text}"
		with open(output_file_name, "a", encoding="utf-8") as out_object:
			out_object.write(clean_line + "\n")

		print("Added.\n")

def read_games_as_dicts(file_name="igrice_valid.txt"):
	games_list = []
	with open(file_name, "r", encoding="utf-8") as file_object:
		for line_text in file_object:
			line_text = line_text.strip()
			if not line_text:
				continue
			parts_list = line_text.split(";")
			if len(parts_list) != 5:
				continue

			name_text, rating_text, year_text, publisher_text, genres_text = parts_list
			try:
				rating_value = float(rating_text)
				year_value = int(year_text)
			except ValueError:
				continue

			genres_list = [g for g in genres_text.split(" ") if g.strip() != ""]

			game_dict = {
				"naziv": name_text,
				"ocjena": rating_value,
				"godina": year_value,
				"izdavac": publisher_text,
				"zanrovi": genres_list
			}
			games_list.append(game_dict)
	return games_list

def show_games_dicts(games_list):
	if len(games_list) == 0:
		print("nema trazenih igrica")
		return
	index_value = 1
	for element in games_list:
		name_text = element["naziv"]
		rating_value = element["ocjena"]
		year_value = element["godina"]
		publisher_text = element["izdavac"]
		genres_list = element["zanrovi"]
		genres_join = " ".join(genres_list)
		print(f"{index_value}. {name_text} | {rating_value:.2f} | {year_value} | {publisher_text} | {genres_join}")
		index_value += 1

def filter_menu(games_list):
	while True:
		print("Igrice vece od unijetog broja")
		print("Naziv igrice")
		print("Godina izdavanja")
		print("Izdavac")
		print(" Zanr (jedan od 3)")
		print("Exit")
		user_choice = input("> ").strip().lower()

		if user_choice == "q":
			break

		if user_choice == "1":
			term_text = input("Unesi naziv: ").strip().lower()
			result_list = []
			for element in games_list:
				if element["naziv"].lower().startswith(term_text):
					result_list.append(element)
			show_games_dicts(result_list)

		elif user_choice == "2":
			print("Unesi minimalnu ocjenu: (izmedju 1.0 i 10.0)")
			rating_text = input("> ").strip()
			if not is_valid_rating_text(rating_text):
				print("error has occured")
				continue
			min_rating = float(rating_text)
			result_list = []
			for element in games_list:
				if element["ocjena"] > min_rating:
					result_list.append(element)
			show_games_dicts(result_list)

		elif user_choice == "3":
			year_text = input("Unesite godinu").strip()
			try:
				year_value = int(year_text)
			except ValueError:
				print("Error has occured")
				continue
			print("Igrice prije ili poslije date godine")
			mode_text = input("> ").strip().lower()
			if mode_text not in ["prije", "poslije"]:
				print("Err: unesi 'prije' ili 'poslije'.")
				continue
			result_list = []
			for element in games_list:
				if mode_text == "prije":
					if element["godina"] < year_value:
						result_list.append(element)
				else:
					if element["godina"] > year_value:
						result_list.append(element)
			show_games_dicts(result_list)

		elif user_choice == "4":
			term_text = input("Unesi izdavaca: ").strip().lower()
			result_list = []
			for element in games_list:
				if element["izdavac"] and element["izdavac"].lower().startswith(term_text):
					result_list.append(element)
			show_games_dicts(result_list)

		elif user_choice == "5":
			print("Mozete unijeti samo sljedece zanrove:", ", ".join(ALLOWED_GENRES))
			input_text = input("Zanrovi samo izmedju 1 i 3: ").strip()
			genres_query = [g for g in input_text.split(" ") if g.strip() != ""]
			if len(genres_query) == 0 or len(genres_query) > 3:
				print("Error has occured. Genres")
				continue
			lower_allowed = [x.lower() for x in ALLOWED_GENRES]
			is_ok = True
			for element in genres_query:
				if element.lower() not in lower_allowed:
					is_ok = False
					break
			if not is_ok:
				print("Err")
				continue

			result_list = []
			for game_item in games_list:
				game_genres_lower = [x.lower() for x in game_item["zanrovi"]]
				all_present = True
				for needed in genres_query:
					if needed.lower() not in game_genres_lower:
						all_present = False
						break
				if all_present:
					result_list.append(game_item)
			show_games_dicts(result_list)

		else:
			print("Odabrali ste nevalidnu opciju.")

def main():
	print("Filtriranje pocetnog fajla i kreiranje 'igrice_valid.txt'")
	valid_lines = clean_and_copy_games("igrice.txt", "igrice_valid.txt")
	if len(valid_lines) == 0:
		print("Nema validnih unosa u početnom fajlu ili fajl ne sadrzi podatke.")
	else:
		print("\nValidne igre (posle filtriranja):")
		print_lines_simple(valid_lines)

	prompt_add_new_games("igrice_valid.txt")

	print("\n Loading igrica iz 'igrice_valid.txt' u listu objekata . . .")
	games_list = read_games_as_dicts("igrice_valid.txt")
	print(f"Ucitano je {len(games_list)} igrica.\n")

	filter_menu(games_list)
	print("\nKraj.")

if __name__ == "__main__":
	main()
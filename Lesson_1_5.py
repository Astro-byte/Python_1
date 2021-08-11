"""5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят 
и сколько между ними находится букв."""

ALPHABET_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

print('''Привет! Данная программа позволит тебе выяснить, 
на каких позициях стоят буквы в алфавите
и сколько между ними находится букв.\nПока используй только русский буквы! 
Начнём!''')

start_char = input("Введите начальный символ: ")
end_char = input("Введеите конечный символ: ")

start_char_position = ALPHABET_RUS.find(start_char.lower()) + 1
end_char_position = ALPHABET_RUS.find(end_char.lower()) + 1

print(f"Позиция в алфавите начального символа: {start_char_position}")
print(f"Позиция в алфавите конечного символа: {end_char_position}")
print(f"Разница в позициях: {end_char_position - start_char_position }")
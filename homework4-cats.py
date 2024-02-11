import  re
from    pathlib import Path

def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                # ідентифікатор, ім'я та вік кота
                cat_id, name, age = line.strip().split(',')
                # словник з інформацією про кота
                cat_info = {"id": cat_id, "name": name, "age": age}
                # Додати словник до списку
                cats_info.append(cat_info)
    
    except FileNotFoundError:
        print("Файл не знайдено.")
        return None
    
    except Exception as e:
        print("Виникла помилка під час обробки файлу:", e)
        return None
    
    return cats_info

# Приклад використання:
cats_info = get_cats_info("C:\\Projects\\vscode-basics\\cats.txt")
if cats_info:
    print(cats_info)
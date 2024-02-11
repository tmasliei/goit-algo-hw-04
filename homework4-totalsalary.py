# Створюємо функцію загальна зарплата (total salary)
def total_salary(path):
    numeric_values = []
    try:
        with open(path, "r") as fh:
            lines = [el.strip() for el in fh.readlines()]
            print(lines)
            for item in lines:
                parts = item.split(',')
                numeric_value = int(parts[1])
                numeric_values.append(numeric_value)
        
        # Загальна сума числових значень
        total_salary = sum(numeric_values)
        
        
        # Середня сума числових значень
        try:
            average_sum = total_salary / len(numeric_values)
        except ZeroDivisionError as e:
            average_sum = 0
            print("Не вірне використання функції")
            return None  # Повертаємо None у випадку ділення на нуль       
        
        return total_salary, average_sum  # Повертаємо обидва значення
    except (IndexError, ValueError) as e:
        print(f"Помилка обробки рядка '{item}': {e}")
        return None  # Повертаємо None у випадку помилки

# Викликаємо функцію total_salary зі шляхом до файлу
result = total_salary("C:\\Projects\\vscode-basics\\salary_work.txt")
if result is not None:
    total_salary_value, average_sum_value = result
    print("Загальна сума числових значень:", total_salary_value)
    print("Середня сума числових значень:", average_sum_value)

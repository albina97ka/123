import tkinter as tk

from tkinter import messagebox

# Создаем главное окно

window = tk.Tk()

window.title("Моя анкета")

window.geometry("400x400")

tk.Label(window, text="Ваше имя:").pack()

# Поле, куда можно ввести текст

name_entry = tk.Entry(window)

name_entry.pack()

level_var = tk.StringVar(value="beginner")  # По умолчанию "Начинающий"

tk.Label(window, text="Ваш уровень:").pack()

# Варианты выбора

levels = [

    ("Начинающий", "junior"),

    ("Средний", "middie"),

    ("Продвинутый", "senior")

]

# Создаем радиокнопки

for text, value in levels:
    tk.Radiobutton(window, text=text, variable=level_var, value=value).pack(anchor="w")

# Переменные для галочек (1 = выбрано, 0 = нет)

python_var = tk.IntVar()

java_var = tk.IntVar()

cpp_var = tk.IntVar()

# Надпись "Какие технологии знаешь?"

tk.Label(window, text="Какие технологии знаешь?").pack()

# Создаем галочки

tk.Checkbutton(window, text="Python", variable=python_var).pack(anchor="w")

tk.Checkbutton(window, text="Java", variable=java_var).pack(anchor="w")

tk.Checkbutton(window, text="C++", variable=cpp_var).pack(anchor="w")


def submit():
    # Получаем имя

    name = name_entry.get()

    # Проверяем, введено ли имя

    if not name:
        messagebox.showerror("Ошибка", "Введи имя!")

        return

    # Получаем уровень

    level = level_var.get()

    # Получаем выбранные технологии

    techs = []

    if python_var.get() == 1: techs.append("Python")

    if java_var.get() == 1: techs.append("Java")

    if cpp_var.get() == 1: techs.append("C++")

    # Показываем результат

    messagebox.showinfo(

        "Твои данные",

        f"Привет, {name}!\n"

        f"Твой уровень: {level}\n"

        f"Технологии: {', '.join(techs) if techs else 'пока нет'}"

    )


# Кнопка "Отправить"

tk.Button(window, text="Отправить", command=submit).pack(pady=10)

window.mainloop()
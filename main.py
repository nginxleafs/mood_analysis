import pandas as pd
import os
from pathlib import Path

DATAFRAME_PATH = Path("~/Documents/mood_analysis/statistics.csv").expanduser()
DATAFRAME_PATH.parent.mkdir(parents=True, exist_ok=True)

if not os.path.exists(DATAFRAME_PATH):
    columns = [
        "Day of the week",
        "Mood",
        "Motivation",
        "Fatigue",
        "Anxiety",
        "Happiness",
    ]
    new_df = pd.DataFrame(columns=columns)
    new_df.to_csv(DATAFRAME_PATH)

df = pd.read_csv(DATAFRAME_PATH)

while True:
    day_of_the_week = input(
        "Введите день недели, где 1 - понедельник, а 7 - воскресение: "
    )
    try:
        day_of_the_week = int(day_of_the_week)
    except ValueError:
        print("День недели должен быть указан одной цифрой.")
        continue
    if 1 <= day_of_the_week <= 7:
        break
    else:
        print("День должен быть указан в диапазоне 1 и 7.")

while True:
    mood = input("Укажите уровень вашего настроения от 0 до 10: ")
    try:
        mood = int(mood)
    except ValueError:
        print("Настроение должно быть указано цифрой, по шкале от 1 до 10.")
        continue
    if 1 <= mood <= 10:
        break
    else:
        print("Настроение должно быть указано в диапазоне 1 и 10.")


while True:
    motivation = input("Укажите уровень вашей мотивации от 0 до 10: ")
    try:
        motivation = int(motivation)
    except ValueError:
        print("Мотивация должна быть указанa цифрой, по шкале от 1 до 10.")
        continue
    if 1 <= motivation <= 10:
        break
    else:
        print("Мотивация должна быть указанa в диапазоне 1 и 10.")

while True:
    fatigue = input("Укажите уровень вашей усталости от 0 до 10: ")
    try:
        fatigue = int(fatigue)
    except ValueError:
        print("Усталость должна быть указанa цифрой, по шкале от 1 до 10.")
        continue
    if 1 <= fatigue <= 10:
        break
    else:
        print("Усталость должна быть указанa в диапазоне 1 и 10.")


while True:
    anxiety = input("Укажите уровень вашей раздраженности от 0 до 10: ")
    try:
        anxiety = int(anxiety)
    except ValueError:
        print("Раздраженность должна быть указанa цифрой, по шкале от 1 до 10.")
        continue
    if 1 <= anxiety <= 10:
        break
    else:
        print("Раздраженность должна быть указанa в диапазоне 1 и 10.")

while True:
    happiness = input("Укажите уровень вашего счастья от 0 до 10: ")
    try:
        happiness = int(happiness)
    except ValueError:
        print("Уровень счастья должен быть указан цифрой, по шкале от 1 до 10.")
        continue
    if 1 <= happiness <= 10:
        break
    else:
        print("Уровень счастья должен быть указан в диапазоне 1 и 10.")


new_row = {
    "Day of the week": day_of_the_week,
    "Mood": mood,
    "Motivation": motivation,
    "Fatigue": fatigue,
    "Anxiety": anxiety,
    "Happiness": happiness,
}

df.loc[len(df)] = new_row
df.to_csv(DATAFRAME_PATH, index=False)

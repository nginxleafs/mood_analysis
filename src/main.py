import pandas as pd
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


def required(var: str):
    try:
        return str(os.getenv(var))
    except ValueError:
        print(".env variable should be set: ", var)
        sys.exit(1)


STATISTICS_PATH = Path(required("STATISTICS_PATH")).expanduser()
STATISTICS_PATH.parent.mkdir(parents=True, exist_ok=True)

if not os.path.exists(STATISTICS_PATH):
    columns = [
        "Day of the week",
        "Mood",
        "Motivation",
        "Fatigue",
        "Anxiety",
        "Happiness",
    ]
    new_df = pd.DataFrame(columns=columns)
    new_df.to_csv(STATISTICS_PATH)

df = pd.read_csv(STATISTICS_PATH)

while True:
    day_of_the_week = input("Enter day of the week, where 1 - monday , а 7 - sunday: ")
    try:
        day_of_the_week = int(day_of_the_week)
    except ValueError:
        print("Day of the week has to be a number.")
        continue
    if 1 <= day_of_the_week <= 7:
        break
    else:
        print("Day has to be inputed in diapazone in range 1 and 7.")

while True:
    mood = input("Enter your mood level, from 1 to 10: ")
    try:
        mood = int(mood)
    except ValueError:
        print("Mood has to be inputed as a number.")
        continue
    if 1 <= mood <= 10:
        break
    else:
        print("Mood has to be in range 1 and 10.")


while True:
    motivation = input("Enter your motivation level, from 1 to 10: ")
    try:
        motivation = int(motivation)
    except ValueError:
        print("Motivation has to inputed as a number.")
        continue
    if 1 <= motivation <= 10:
        break
    else:
        print("Motivation has to be in range 1 and 10.")

while True:
    fatigue = input("Enter you fatigue level, from 1 to 10: ")
    try:
        fatigue = int(fatigue)
    except ValueError:
        print("Fatigue has to be inputed as a number.")
        continue
    if 1 <= fatigue <= 10:
        break
    else:
        print("Fatigue has to be in range 1 and 10.")


while True:
    anxiety = input("Enter you anxiety level, from 1 to 10: ")
    try:
        anxiety = int(anxiety)
    except ValueError:
        print("Anxiety has to be inputed as a number.")
        continue
    if 1 <= anxiety <= 10:
        break
    else:
        print("Anxiety has to be in range 1 and 10.")

while True:
    happiness = input("Enter you happiness level, from 1 to 10: ")
    try:
        happiness = int(happiness)
    except ValueError:
        print("Happiness level has to be inputed as a number.")
        continue
    if 1 <= happiness <= 10:
        break
    else:
        print("Happiness level has to be in range 1 and 10.")


new_row = {
    "Day of the week": day_of_the_week,
    "Mood": mood,
    "Motivation": motivation,
    "Fatigue": fatigue,
    "Anxiety": anxiety,
    "Happiness": happiness,
}

df.loc[len(df)] = new_row
df.to_csv(STATISTICS_PATH, index=False)

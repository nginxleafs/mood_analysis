from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from pathlib import Path
from dotenv import load_dotenv

import pandas as pd
import os
import sys

load_dotenv()


class Statistics:
    def __init__(self) -> None:
        self.day_of_the_week: int
        self.mood: int
        self.motivation: int
        self.fatigue: int
        self.anxiety: int
        self.happiness: int

    def to_dict(self):
        return {
            "Day of the week": self.day_of_the_week,
            "Mood": self.mood,
            "Motivation": self.motivation,
            "Fatigue": self.fatigue,
            "Anxiety": self.anxiety,
            "Happiness": self.happiness,
        }


def required(var: str) -> str:
    try:
        return str(os.getenv("STATISTICS_PATH"))
    except ValueError:
        print(f"The env variables is not set: {var}")
        sys.exit(1)


def save_statistics(statistics: Statistics):
    if not os.path.exists(STATISTICS_PATH):
        create_dataframe_file()
    df = pd.read_csv(STATISTICS_PATH)
    df.loc[len(df)] = statistics.to_dict()
    df.to_csv(STATISTICS_PATH, index=False)


def create_dataframe_file():
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


STATISTICS_PATH = Path(required("STATISTICS_PATH")).expanduser()

STATISTICS_PATH.parent.mkdir(exist_ok=True, parents=True)
if not os.path.exists(STATISTICS_PATH):
    create_dataframe_file()


class Application(App):
    def build(self):
        self.statistics = Statistics()
        sm = ScreenManager()
        sm.add_widget(DayInputScreen(name="day_input"))
        sm.add_widget(MoodInputScreen(name="mood_input"))
        sm.add_widget(MotivationInputScreen(name="motivation_input"))
        sm.add_widget(FatigueInputScreen(name="fatigue_input"))
        sm.add_widget(AnxietyInputScreen(name="anxiety_input"))
        sm.add_widget(HappinessInputScreen(name="happiness_input"))
        sm.add_widget(ResultScreen(name="result_screen"))
        return sm


class DayInputScreen(Screen):
    def __init__(self, **kwargs):
        super(DayInputScreen, self).__init__(**kwargs)
        self.label = Label(
            text="Enter day of the week, where 1 - monday , а 7 - sunday: ",
        )
        self.input = TextInput(hint_text="In range 1 and 10", multiline=False)
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=20)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        week_day = self.input.text
        if week_day.isdigit() and 1 <= int(week_day) <= 7:
            App.get_running_app().statistics.day_of_the_week = int(week_day)
            self.manager.current = "mood_input"


class MoodInputScreen(Screen):
    def __init__(self, **kwargs):
        super(MoodInputScreen, self).__init__(**kwargs)
        self.label = Label(text="Enter your mood level, from 1 to 10: ")
        self.input = TextInput(hint_text="In range 1 to 10")
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=50)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        mood = self.input.text
        if mood.isdigit() and 1 <= int(mood) <= 10:
            App.get_running_app().statistics.mood = int(mood)
            self.manager.current = "motivation_input"


class MotivationInputScreen(Screen):
    def __init__(self, **kwargs):
        super(MotivationInputScreen, self).__init__(**kwargs)
        self.label = Label(text="Enter your motivation level, from 1 to 10: ")
        self.input = TextInput(hint_text="1 - low, 10 - high")
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=50)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        motivation = self.input.text
        if motivation.isdigit() and 1 <= int(motivation) <= 10:
            App.get_running_app().statistics.motivation = int(motivation)
            self.manager.current = "fatigue_input"


class FatigueInputScreen(Screen):
    def __init__(self, **kwargs):
        super(FatigueInputScreen, self).__init__(**kwargs)
        self.label = Label(text="Enter your current fatigue level, from 1 to 10: ")
        self.input = TextInput(hint_text="1 - low, 10 - high")
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=50)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        fatigue = self.input.text
        if fatigue.isdigit() and 1 <= int(fatigue) <= 10:
            App.get_running_app().statistics.fatigue = int(fatigue)
            self.manager.current = "anxiety_input"


class AnxietyInputScreen(Screen):
    def __init__(self, **kwargs):
        super(AnxietyInputScreen, self).__init__(**kwargs)
        self.label = Label(text="Enter your current anxiety level, from 1 to 10: ")
        self.input = TextInput(hint_text="1 - low, 10 - high")
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=50)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        anxiety = self.input.text
        if anxiety.isdigit() and 1 <= int(anxiety) <= 10:
            App.get_running_app().statistics.anxiety = int(anxiety)
            self.manager.current = "happiness_input"


class HappinessInputScreen(Screen):
    def __init__(self, **kwargs):
        super(HappinessInputScreen, self).__init__(**kwargs)
        self.label = Label(text="Enter your current happiness level, from 1 to 10: ")
        self.input = TextInput(hint_text="1 - low, 10 - high")
        self.button = Button(text="Enter", on_press=self.on_next)
        self.form = BoxLayout(
            orientation="vertical",
            size_hint=(None, None),
            size=(300, 150),
            spacing=10,
            pos_hint={"center_x": 0.5},
        )
        self.form.add_widget(self.input)
        self.form.add_widget(self.button)
        self.root = BoxLayout(orientation="vertical", padding=20, spacing=50)
        self.root.add_widget(self.label)
        self.root.add_widget(self.form)
        self.add_widget(self.root)

    def on_next(self, instance):
        happiness = self.input.text
        if happiness.isdigit() and 1 <= int(happiness) <= 10:
            statistics = App.get_running_app().statistics
            statistics.happiness = int(happiness)
            save_statistics(statistics)
            self.manager.current = "result_screen"


class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.label = Label(text=f"Thanks, your data saved to {STATISTICS_PATH}")
        self.add_widget(self.label)


if __name__ == "__main__":
    Application().run()

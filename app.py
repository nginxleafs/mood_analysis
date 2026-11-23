from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout

import pandas as pd
import os

STATISTICS_PATH = "statistics.csv"


class Statistics:
    day_of_the_week = int
    mood = int
    motivation = int
    fatigue = int
    anxiety = int
    happiness = int


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
            text="Введите день недели, где 1 - понедельник, 7 - воскресенье:",
        )
        self.input = TextInput(hint_text="1 до 7.", multiline=False)
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text="Введите вашe текущуу настроение:")
        self.input = TextInput(hint_text="1 - очень плохое, 10 - очень хорошо.")
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text="Введите вашу текущую мотивацию:")
        self.input = TextInput(hint_text="1 - очень низкая, 10 - очень высокая.")
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text="Введите вашу текущую усталость:")
        self.input = TextInput(hint_text="1 - очень низкая, 10 - очень высокая.")
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text="Введите вашу текущую раздражённость: ")
        self.input = TextInput(hint_text="1 - очень низкая, 10 - очень высокая.")
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text="Введите ваш уровень счастья: ")
        self.input = TextInput(hint_text="1 - очень низкий, 10 - очень высокий.")
        self.button = Button(text="Ввод", on_press=self.on_next)
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
        self.label = Label(text=f"Спасибо, данные сохранены в {STATISTICS_PATH}")
        self.add_widget(self.label)


def save_statistics(statistics: Statistics):
    if not os.path.exists(STATISTICS_PATH):
        create_dataframe_file()
    df = pd.read_csv(STATISTICS_PATH)
    new_values = {
        "Day of the week": statistics.day_of_the_week,
        "Mood": statistics.mood,
        "Motivation": statistics.motivation,
        "Fatigue": statistics.fatigue,
        "Anxiety": statistics.anxiety,
        "Happiness": statistics.happiness,
    }
    df.loc[len(df)] = new_values
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


if __name__ == "__main__":
    Application().run()

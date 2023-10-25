import json

from kivymd.app import MDApp
from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import IRightBody, TwoLineAvatarIconListItem


class MainWindow(MDBoxLayout):
    pass

class RightButton(IRightBody, MDIconButton):
    pass

class SearchQuizItem(TwoLineAvatarIconListItem):
    pass

class QuizApp(MDApp):
    def name_search_quiz_list(self, query):
        print(query)
    def show_all_quiz(self):
        app = MDApp.get_running_app()
        result_list_widget = app.root.ids.search_results
        with open('text [MConverter.eu].json') as f:
            templates = json.load(f)
        quizs = templates['quizs']
        for i in quizs:
            quiz = quizs[i]

            name = quiz['name']
            count = len(quiz['quiz'])
            quizСount = 'Количество вопросов - ' + str(count)
            result_list_widget.add_widget(
                SearchQuizItem(text=name, secondary_text=quizСount)
            )
    def build(self):

        return MainWindow()

if __name__ == '__main__':
    QuizApp().run()
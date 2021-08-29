from kivy.app import App
from auth.auth import Authentification


class MainApp(App):
    auth = Authentification()

    def build(self):
        return self.auth



MainApp().run()

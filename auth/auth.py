from kivy.uix.widget import Widget
from kivy.lang import Builder
import sqlite3



# load auth kv files
Builder.load_file('auth/auth.kv')

class Authentification(Widget):

    def db_connect(self, db_path):
        self.db = sqlite3.connect(db_path)
        self.cur = self.db.cursor()

    def db_disconnect(self):
        self.db.close()

    @staticmethod
    def valid_user(user):
        return True

    @staticmethod
    def valid_password(password):
        return True

    def authenticate(self, user, password):
        if not self.valid_user(user) or not self.valid_password(password):
            return False
        
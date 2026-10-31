import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest
from streamlit.proto.TextInput_pb2 import TextInput

from academy.catalog import QUIZZES

APP = str(Path(__file__).resolve().parents[1] / "app.py")


class AcademySmokeTests(unittest.TestCase):
    def app(self):
        app = AppTest.from_file(APP).run(timeout=20)
        self.assertFalse(app.exception)
        return app

    def test_home_and_navigation(self):
        app = self.app()
        self.assertEqual(app.session_state["page"], "home")
        app.button(key="discover_tests").click().run()
        self.assertFalse(app.exception)
        self.assertEqual(app.session_state["page"], "tests")
        self.assertTrue(any(b.key == "start_sql-basics" and b.disabled for b in app.button))

    def test_catalog_search_filters_cards(self):
        app = self.app()
        app.button(key="nav_tests").click().run()
        app.text_input[0].set_value("PL/SQL").run()
        self.assertFalse(app.exception)
        starts = [b for b in app.button if b.key and b.key.startswith("start_")]
        self.assertEqual([b.key for b in starts], ["start_plsql"])
        app.text_input[0].set_value("no-such-test").run()
        self.assertTrue(any("Uyğun test tapılmadı" in item.value for item in app.info))

    def test_login_is_honest_preview(self):
        app = self.app()
        app.button(key="header_login").click().run()
        self.assertEqual(app.session_state["page"], "login")
        self.assertFalse(app.exception)
        self.assertEqual(app.text_input[1].proto.type, TextInput.PASSWORD)
        app.text_input[0].set_value("demo@example.com")
        app.text_input[1].set_value("not-a-real-password")
        next(b for b in app.button if b.label == "Daxil ol →").click().run()
        self.assertFalse(app.exception)
        self.assertTrue(any("Giriş hələ aktiv deyil" in item.value for item in app.info))
        with self.assertRaises(KeyError):
            _ = app.session_state["user"]

    def test_results_and_no_public_admin_menu(self):
        app = self.app()
        self.assertFalse(any("Müəllim" in b.label or "Sual bankı" in b.label for b in app.button))
        app.button(key="nav_results").click().run()
        self.assertFalse(app.exception)
        app.button(key="results_login").click().run()
        self.assertEqual(app.session_state["page"], "login")

    def test_public_metadata_has_no_answer_keys(self):
        self.assertEqual(len(QUIZZES), 3)
        for quiz in QUIZZES:
            self.assertNotIn("correct", quiz)
            self.assertNotIn("answers", quiz)


if __name__ == "__main__":
    unittest.main()

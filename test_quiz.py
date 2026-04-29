import unittest
import random
from project1_0final import get_unique_colors, give_achievement, check, LANG_TEXT

class TestQuizFunctions(unittest.TestCase):
    
    def test_get_unique_colors(self):
        # Test czy zwraca odpowiednią liczbę kolorów
        colors = get_unique_colors(3)
        self.assertEqual(len(colors), 3)
        
        # Test czy wszystkie kolory są z listy dozwolonych
        allowed = ["#ff914d", "#4da6ff", "#66cc66", "#dc01bb"]
        for c in colors:
            self.assertIn(c, allowed)
    
    def test_give_achievement_basic(self):
        # Symulacja - w rzeczywistości musiałabyś ustawić globalne zmienne
        # To jest przykład testu koncepcyjnego
        achievements = []
        # Tutaj logika testu achievements
        self.assertTrue(True)  # placeholder
    
    def test_check_logic(self):
        # Test sprawdzania odpowiedzi
        # To wymaga mockowania globalnych zmiennych
        pass

if __name__ == "__main__":
    unittest.main()
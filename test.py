from unittest import TestCase
from app import app
from flask import session
from boggle import Boggle


class FlaskTests(TestCase):

    def test_start_page(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1 class="game-name">BOGGLE</h1>', html)
    
    def test_gameboard(self):
        with app.test_client() as client:
            resp = client.get('/boggle')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<table class="game-board">', html)
            self.assertTrue(session['game_board'])


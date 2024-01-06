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

    def test_guess_valid(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['game_board'] = [['F', 'O', 'N', 'R', 'M'],
                                                ['H', 'N', 'T', 'U', 'T'], 
                                                ['E', 'C', 'Q', 'O', 'C'],
                                                ['H', 'A', 'T', 'U', 'E'], 
                                                ['R', 'S', 'E', 'O', 'R']]
                test_data = {'guess': 'hat'}
                response = client.post('/guess', json=test_data)
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data, {'result': 'ok'})

    def test_guess_not_word(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['game_board'] = [['F', 'O', 'N', 'R', 'M'],
                                                ['H', 'N', 'T', 'U', 'T'], 
                                                ['E', 'C', 'Q', 'O', 'C'],
                                                ['H', 'A', 'T', 'U', 'E'], 
                                                ['R', 'S', 'E', 'O', 'R']]
                test_data = {'guess': 'qtc'}
                response = client.post('/guess', json=test_data)
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data, {'result': 'not-word'})

    def test_guess_not_board(self):
        with app.test_client() as client:
            with client.session_transaction() as change_session:
                change_session['game_board'] = [['F', 'O', 'N', 'R', 'M'],
                                                ['H', 'N', 'T', 'U', 'T'], 
                                                ['E', 'C', 'Q', 'O', 'C'],
                                                ['H', 'A', 'T', 'U', 'E'], 
                                                ['R', 'S', 'E', 'O', 'R']]
                test_data = {'guess': 'phone'}
                response = client.post('/guess', json=test_data)
                data = response.get_json()

                self.assertEqual(response.status_code, 200)
                self.assertEqual(data, {'result': 'not-on-board'})
    
    def test_game_over(self):
        with app.test_client() as client:
            test_data = {'score': 250}
            response = client.post('/gameover', json=test_data)
            data = response.get_json()
            print(data)

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, {'result': 'score logged'})
            self.assertEqual(session['high_score'], 250)
            self.assertTrue(session['games_played'])
        
        with client.session_transaction() as change_session:
            change_session['high_score'] = 51
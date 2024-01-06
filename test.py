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

            self.assertEqual(response.status_code, 200)
            self.assertEqual(data, {'result': 'score logged'})
            self.assertEqual(session['high_score'], 250)
            self.assertTrue(session['games_played'])
        
        with client.session_transaction() as change_session:
            change_session['high_score'] = 51


class BoggleTests(TestCase):

    def test_read_dict(self):
        test_game = Boggle()
        self.assertIn('Aaronitic', test_game.read_dict("words.txt"))

    def test_make_board(self):
        test_game = Boggle()
        board = test_game.make_board()
        self.assertEqual(len(board), 5)
        self.assertEqual(len(board[2]), 5)
        self.assertIsInstance(board[0][2], str)

    
    def test_check_valid_word(self):
        test_game = Boggle()
        board = [['F', 'O', 'N', 'R', 'M'],
                ['H', 'N', 'T', 'U', 'T'], 
                ['E', 'C', 'Q', 'O', 'C'],
                ['H', 'A', 'T', 'U', 'E'], 
                ['R', 'S', 'E', 'O', 'R']]
        word = 'hat'
        self.assertEqual(test_game.check_valid_word(board, word), "ok")
        board = [['F', 'O', 'N', 'R', 'M'],
                ['H', 'N', 'T', 'U', 'T'], 
                ['E', 'C', 'Q', 'O', 'C'],
                ['H', 'A', 'T', 'U', 'E'], 
                ['R', 'S', 'E', 'O', 'R']]
        word = 'qtc'
        self.assertEqual(test_game.check_valid_word(board, word), "not-word")
        board = [['F', 'O', 'N', 'R', 'M'],
                ['H', 'N', 'T', 'U', 'T'], 
                ['E', 'C', 'Q', 'O', 'C'],
                ['H', 'A', 'T', 'U', 'E'], 
                ['R', 'S', 'E', 'O', 'R']]
        word = 'phone'
        self.assertEqual(test_game.check_valid_word(board, word), "not-on-board")

    def test_find(self):
        test_game = Boggle()
        board = [['F', 'O', 'N', 'R', 'M'],
                ['H', 'N', 'T', 'U', 'T'], 
                ['E', 'C', 'Q', 'O', 'C'],
                ['H', 'A', 'T', 'U', 'E'], 
                ['R', 'S', 'E', 'O', 'R']]
        word = 'FON'
        self.assertTrue(test_game.find(board, word))
        word = 'HEH'
        self.assertTrue(test_game.find(board, word))
        word = 'FNQUCO'
        self.assertTrue(test_game.find(board, word))
        word = 'KITTY'
        self.assertFalse(test_game.find(board, word))

    def test_find_from(self):
        test_game = Boggle()
        board = [['F', 'O', 'N', 'R', 'M'],
                ['H', 'N', 'T', 'U', 'T'], 
                ['E', 'C', 'Q', 'O', 'C'],
                ['H', 'A', 'T', 'U', 'E'], 
                ['R', 'S', 'E', 'O', 'R']]
        word = 'FON'
        seen = set()
        self.assertTrue(test_game.find_from(board, word, 0, 0, seen))
        word = 'UCT'
        self.assertFalse(test_game.find_from(board, word, 0, 0, seen))
from app import db
import datetime

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player1 = db.Column(db.String(50), nullable=False)
    player2 = db.Column(db.String(50), nullable=False)
    player1_score = db.Column(db.Integer, default=0)
    player2_score = db.Column(db.Integer, default=0)
    grid = db.Column(db.String(100), nullable=False)  # Store 4x4 grid as string
    start_time = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    valid_words = db.Column(db.Text)  # Store valid words as JSON string

    def __repr__(self):
        return f'<Game {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'players': [self.player1, self.player2],
            'scores': [self.player1_score, self.player2_score],
            'grid': self.grid.split(','),  # Convert to 4x4 array
            'time_remaining': 180 - (datetime.datetime.utcnow() - self.start_time).seconds
        }

    @staticmethod
    def generate_grid():
        # Implement your Boggle dice logic here
        return ','.join(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'])

    def is_valid_word(self, word):
        # Implement word validation against dictionary
        return word.lower() in self.load_dictionary()

    @staticmethod
    def load_dictionary():
        with open('app/wordlist.txt') as f:
            return set(word.strip().lower() for word in f)

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #games_played = db.relationship('Game', backref='player', lazy=True)

    def __repr__(self):
        return f'<Player {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            #'games_played': [game.to_dict() for game in self.games_played]
        }
from flask import request, jsonify
from models import Game, Player
from app import db


def init_routes(app):
    @app.route('/api', methods=['GET'])
    def index():
        return jsonify({'message': 'Welcome to Boggle Battle API!'})
    
    @app.route('/api/new-game', methods=['POST'])
    def new_game():
        data = request.json
        game = Game(
            player1=data['player1'],
            player2=data['player2'],
            grid=Game.generate_grid()
        )
        db.session.add(game)
        db.session.commit()
        return jsonify(game.to_dict()), 201
    
    @app.route('/api/new-player', methods=['POST'])
    def new_player():
        data = request.json
        player = Player(name=data['name'])
        db.session.add(player)
        db.session.commit()
        return jsonify(player.to_dict()), 201

    @app.route('/api/submit-word', methods=['POST'])
    def submit_word():
        data = request.json
        game = Game.query.get(data['game_id'])

        if not game:
            return jsonify({'error': 'Game not found'}), 404

        if game.is_valid_word(data['word']):
            # Implement scoring logic
            return jsonify({'valid': True, 'score': len(data['word'])})

        return jsonify({'valid': False})

    @app.route('/api/game-status/<int:game_id>')
    def game_status(game_id):
        game = Game.query.get(game_id)
        return jsonify(game.to_dict())
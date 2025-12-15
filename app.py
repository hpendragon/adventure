from flask import Flask, render_template, request, jsonify
from game.player import Player
from game.aidm import AIDM
from game.inventory import InventorySystem

app = Flask(__name__)
app.config.from_object('config')

# Initialize game systems
player = Player()
aidm = AIDM()
inventory = InventorySystem()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game/action', methods=['POST'])
def game_action():
    data = request.json
    action = data.get('action')
    response = aidm.process_action(action, player)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

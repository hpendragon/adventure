from flask import Flask, render_template, request, jsonify
from game.player import Player
from game.aidm import AIDM
from game.story import create_basic_story

app = Flask(__name__)

# Initialize game systems
story = create_basic_story()  # We'll create this function
player = Player()
aidm = AIDM(story)

@app.route('/')
def home():
    initial_node = story.get_current_node()
    return render_template('index.html')

@app.route('/game/action', methods=['POST'])
def game_action():
    data = request.json
    action = data.get('action')
    response = aidm.process_action(action, player)
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

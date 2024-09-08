"""Flask webapp for frontend."""

import secrets

import family_business as fb
import flask

app = flask.Flask(__name__)
app.secret_key = secrets.token_hex(6)


# Top-level templates
@app.route('/')
def index():
  flask.session['username'] = 'brett'
  
  if not flask.session.get('username'):
    return flask.render_template('login.html')
  name = flask.session.get('username')
  if not flask.session.get('lobby'):
    return flask.render_template('lobby.html', name=name)
  lobby = flask.session.get('lobby')
  return flask.render_template('game.html', name=name, lobby=lobby)


@app.route('/login', methods=['POST'])
def login():
  username = flask.request.form.get('name')
  try:
    MANAGER.add_player(username)
  except ValueError as e:
    print(e)
    return flask.make_response(str(e), 400)
  flask.session['username'] = username
  return flask.make_response('OK', 200)


@app.route('/logout', methods=['GET', 'POST'])
def logout():
  flask.session.pop('username', None)
  flask.session.pop('lobby', None)
  return flask.redirect('/')


@app.route('/join', methods=['POST'])
def join_game():
  """Create a game if not exists, and add player to the game."""
  lobby = flask.request.form.get('lobby')

  # Lookup the lobby name, create game if not exists.
  game = MANAGER.get_game(lobby)
  if not game:
    game = MANAGER.new_game(lobby)
  flask.session['lobby'] = lobby

  name = flask.session.get('username')
  player = MANAGER.get_player(name)
  game.add_player(player)
  return flask.jsonify({})


@app.route('/game/<name>')
def get_game(name: str):
  return flask.render_template('game.html', name=name)


@app.route('/game/<name>/state')
def get_game_state(name):
  return flask.jsonify(MANAGER.get_game_state(name))


@app.route('/game/<name>/ready')
def get_game_readiness(name):
  return flask.jsonify(MANAGER.get_game_state(name))


# Per-game actions
@app.route('/game/<name>/players')
def get_players():
  data = {
      'players': [],
  }
  return flask.jsonify(data)


@app.route('/game/<name>/hitlist')
def get_hitlist():
  data = {
      'hitlist': [],
  }
  return flask.jsonify(data)


class GameManager:
  """Manager for multiple games."""

  def __init__(self):
    self._games = {}
    self._players = {}

  def add_player(self, name):
    if name in self._players:
      raise ValueError('%s is taken.' % name)
    self._players[name] = fb.Player(name)

  def get_player(self, name):
    if name not in self._players:
      return None
    return self._players[name]

  def new_game(self, name):
    game = fb.Game()
    self._games[name] = game
    return game

  def get_game_state(self, name):
    game = self.get_game(name)
    if not game:
      return None
    return game.get_state()

  def get_game(self, name):
    if name not in self._games:
      return None
    game = self._games[name]
    return game


MANAGER = GameManager()

# Test state
MANAGER.new_game('test')
MANAGER.add_player('brett')
MANAGER.add_player('other')

# flask.session['username'] = 'brett'
# flask.session['lobby'] = 'test'

if __name__ == '__main__':
  app.run(debug=True)

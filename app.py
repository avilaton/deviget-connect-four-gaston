

import os
from flask import Flask, render_template, abort, request, redirect
from connect_four import ConnectFour

app = Flask(__name__)
game = ConnectFour()


@app.route('/games/1', defaults={'player': 1, 'color': 'YELLOW'})
@app.route('/games/2', defaults={'player': 2, 'color': 'RED'})
def player(player, color):
    if player not in [1, 2]:
        abort(404)

    pick = request.args.get('column', type=int)
    if game.turn is color:
        print game.turn
        if pick:
            game.move(pick)
            print('redirect')
            return redirect('/games/' + str(player))

    return render_template('play.html', player=player, color=color, game=game)


@app.route('/')
def home():
    global game
    game = ConnectFour()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def check_win():
	if x == 9:
		return "not"
        for i in range(0,9,3):
                if board[i] == board[i+1] == board[i+2]:
                        return [board[i], i, i+1, i+2]
        for i in range(3):
                if board[i] == board[i+3] == board[i+6]:
                        return [board[i], i, i+3, i+6]
        if board[0] == board[4] == board[8]:
                return [board[0], 0, 4, 8]
        if board[2] == board[4] == board[6]:
                return [board[2], 2, 4, 6]

def x_update():
	global x
	x += 1

def turn_of():
	if x%2 == 0:
		return "X"
	else:
		return u'\u2713'
@app.route('/initialize_game')
def initialize_game():
	global board
	global x
	x = 0
	board = [i for i in range(1, 10)]
	return redirect('/')
initialize_game()

def result():
	winner = check_win()[1:]
	if winner == "ot":
		winner=[10]
	print(winner)
	l = []
	for x in range(1,10): 
		for i in winner:
			if x == i+1:
				checker = "on"
				break
			else:
				checker = ""
		if checker:
			l.append(i)
		else:
			l.append(10)
	return l


@app.route('/')
def display_board():
	winner = check_win()
	if winner:
		return redirect('/winner')
	turn = turn_of()
	return render_template("game.html", board=board, turn=turn, tick=u'\u2713')

@app.route('/shail', methods=['POST'])
def shail():
	for pos in request.form:
		pos = int(pos)
	if board[pos-1] == "X" or board[pos-1] == u'\u2713':
		return redirect('/')
	if x%2 == 0:
		board[pos-1] = "X"
	else:
		board[pos-1] = u'\u2713'
	x_update()
	return redirect('/')

@app.route('/winner')
def game_winner():
	game_board = board
	if check_win() == "not":
		msg = ("There is not any winner Ha ha ha!")
	else:
		msg = ("Winner is " +  (check_win()[0]) + " Ha ha ha!")
	alert = ("alert(msg);")
	winner_index=result()
	turn = None
	initialize_game()
	return render_template("winner.html", board=game_board, alert=alert, msg=msg, turn=turn, disabled="disabled", tick=u'\u2713', winner=winner_index)
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=True)
	

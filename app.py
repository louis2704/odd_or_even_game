from flask import Flask, render_template, request

app = Flask(__name__)

# Pass the LND node details as command line arguments or set default values
rpc_user = "default_user"
rpc_password = "default_password"
rpc_path = "localhost:10009"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['GET', 'POST'])
def play():
    if request.method == 'POST':
        guessed_number = int(request.form['number'])
        user_guess = request.form['guess']
        return render_template('play.html', guessed_number=guessed_number, user_guess=user_guess)
    return render_template('play.html')

@app.route('/result', methods=['POST'])
def result():
    guessed_number = int(request.form['number'])
    user_guess = request.form['guess']
    
    # Determine if the guessed number is even or odd
    if guessed_number % 2 == 0:
        server_choice = "even"
    else:
        server_choice = "odd"

    if user_guess == server_choice:
        result = "Congratulations! You guessed correctly."
    else:
        result = "Oops, wrong guess. Try again!"

    return render_template('result.html', guessed_number=guessed_number, user_guess=user_guess, server_choice=server_choice, result=result)

if __name__ == '__main__':
    # Check if command line arguments are provided for LND node details
    import sys

    if len(sys.argv) == 4:
        rpc_user = sys.argv[1]
        rpc_password = sys.argv[2]
        rpc_path = sys.argv[3]

    app.run(debug=True)

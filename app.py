from flask import Flask, render_template, request, redirect, json, session


app = Flask(__name__)
app.secret_key = 'oi23hh23h2d2323-234235'
SESSION_TYPE = 'filesystem'


app.config.from_object(__name__)


def write_to_file(filename, data):
    with open(filename, 'a') as file:
        file.writelines(data)


def check_username_is_unique(username):
    with open('static/users.txt', 'r') as user_list:
        usernames = user_list.readlines()
        for name in usernames:
            if username.strip().lower() == name.strip().lower().split(' ', 1)[0]:
                return False
        return True


def get_next_question(question_number):
    question_information = {}
    with open('static/countries.json', 'r') as json_data:
        questions_data = json.load(json_data)
        for question in questions_data:
            if question['id'] == str(question_number):
                question_information = question
        return question_information


def update_user_score(username):
    with open('static/users.txt', 'r') as file:
        filedata = file.read()
    score_update = username + ' ' + str(session['score'])
    filedata = filedata.replace(username, score_update)
    with open('static/users.txt', 'w') as file:
        file.write(filedata)
    file.close()


def order_the_scores():
    score_table = []
    with open('static/users.txt') as file:
        for line in file:
            name, score = line.split(' ')
            score = int(score)
            score_table.append((name, score))
    score_table.sort(key=lambda s: s[1], reverse=True)
    return score_table


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if check_username_is_unique(request.form['username'] + "\n"):
            write_to_file('static/users.txt', request.form['username'].strip().lower() + "\n")
            session['username'] = request.form['username']
            session['question_number'] = 1
            session['score'] = 0
            return redirect(request.form['username'])
        error_message = 'Please use another name, I\'ll get in a muddle with that one.'
        return render_template('index.html', error = error_message)
    return render_template('index.html')


@app.route('/<username>', methods=['GET', 'POST'])
def questions(username):
    if request.method == 'POST':
        session['score'] += int(request.form['pointsWorth'])
        if session['question_number'] == 10:
            update_user_score(username)
            score_list = order_the_scores()
            return render_template('highscores.html', user=username, high_score=score_list)
        session['question_number'] += 1
        question_information = get_next_question(session['question_number'])
        return render_template('question.html', question=question_information, user=username, score=session['score'])
    question_information = get_next_question(session['question_number'])
    return render_template('question.html', question=question_information, user=username, score=session['score'])


if __name__ == '__main__':
    app.run()
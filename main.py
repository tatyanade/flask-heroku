# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from model import get_outfit

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
  return render_template('index.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
  if request.method == "POST":
    print(request.form)
    user_name = request.form['user_name']
    answer1 = request.form['answer1']
    answer2 = request.form['answer2']
    answer3 = request.form['answer3']
    final_outfit = get_outfit(answer1,answer2,answer3)
    print(final_outfit)
    return render_template("results.html", user_name = user_name, final_outfit=final_outfit)
  else:
    return 'error'


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)

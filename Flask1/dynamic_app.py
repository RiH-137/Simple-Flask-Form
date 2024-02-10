#redirect--> redirect to success page
#url_for--> dynamic url

from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World, this is my Flask app!"

@app.route('/success/<int:score>')
def success(score):
    return "The Person has passed and the marks is" + str(score)                     #http://127.0.0.1:8000/success/97

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is" + str(score)                     #http://127.0.0.1:8000/fail/13

'''Result checker'''
@app.route('/results/<int:score>') 
def results(score):
    results=""
    if score <50:
        results='fail'
    else:                                                                               #http://127.0.0.1:8000//results/1
        results='pass'
    return redirect(url_for(results,score))


if __name__ == '__main__':
    app.run(debug=True, port='8000')


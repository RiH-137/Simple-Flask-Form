#Integrate HTML with Flask
#HTML verb GET and PORT


#request help us to read the posted value


from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('form.html')


###this is my result checker html page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])      # science is id
        maths=float(request.form['maths'])
        c=float(request.form['science'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4

        res=""
        if total_score>=50:
            res="success"
        else:
            res="fail"
        return redirect(url_for(res, score=total_score))
    


@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html', result=res)      #result is the id of output in "result.html"
 



@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is" + str(score)                     #http://127.0.0.1:8000/fail/13



'''Result checker'''
# @app.route('/results/<int:score>') 
# def results(marks):
#     results=""
#     if marks <50:
#         results='fail'
#     else:                                                                               #http://127.0.0.1:8000//results/1
#         results='pass'
#     return redirect(url_for(results,score= marks))




    


if __name__ == '__main__':
    app.run(debug=True)


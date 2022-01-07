from flask import Flask, render_template, request

from DP2 import dynamic_problem2
from gvns1 import GVNS, RVNS
from gvns2 import GVNS2, RVNS2
from dp1 import dynamic_function
from moore import moore1
STATIC_DIR= 'html_css'
app = Flask(__name__,template_folder='html_css',static_folder=STATIC_DIR)
@app.route("/")
def hello():
    return render_template("index.html")
@app.route("/index.html")
def hey():
    return render_template("index.html")

@app.route("/problem1.html")
def p1():
    return render_template("problem1.html")
@app.route("/problem2.html")
def p2():
    return render_template("problem2.html")
@app.route("/DP1.html",methods=("GET","POST"))
def dp1():
    if request.method == 'POST':
        fl = request.files['file']
        lst = fl.stream.readlines()
        numberofele = int(lst[0])
        processTime = lst[1].decode('utf-8').split('\t')
        dueDate = lst[2].decode('utf-8').split('\t')
        sequence,obj = dynamic_function([i for i in range(0,numberofele)],[int(p) for p in processTime],[int(d) for d in dueDate])
        print(sequence,obj)
        return render_template('DP1.html',variable=sequence,fobj=obj)
    elif request.method == 'GET':
        print('from get !!')
        return render_template('DP1.html')

@app.route("/DP2.html", methods=("GET", "POST"))
def dp2():
    if request.method == 'POST':
        fl = request.files['file']
        lst = fl.stream.readlines()
        numberofele = int(lst[0])
        processTime = lst[1].decode('utf-8').split('\t')
        dueDate = lst[2].decode('utf-8').split('\t')
        alpha=lst[3].decode('utf-8').split('\t')
        beta=lst[4].decode('utf-8').split('\t')
        sequence2, obj = dynamic_problem2([i for i in range(0, numberofele)], [int(p) for p in processTime],
                                             [int(d) for d in dueDate],[int(al) for al in alpha],[int(bet) for bet in beta])
        sequence2=sequence2.split(',')
        print(sequence2, obj)
        return render_template('DP2.html', variable=sequence2, fobj=obj)
    elif request.method == 'GET':
        print('from get !!')
        return render_template('DP2.html')
@app.route("/moore.html",methods=("GET","POST"))
def moore():
    if request.method == 'POST':
        fl = request.files['file']
        lst = fl.stream.readlines()
        numberofele = int(lst[0])
        processTime = lst[1].decode('utf-8').split('\t')
        dueDate = lst[2].decode('utf-8').split('\t')
        jobs = [i + 1 for i in range(numberofele)]
        p = [int(i) for i in processTime]
        d = [int(i) for i in dueDate]
        data = [[jobs[i], p[i], d[i]] for i in range(len(jobs))]
        print(data)
        obj,sequence2 = moore1(data)
        print("this is moore",sequence2,obj)
        return render_template('moore.html',v1=sequence2,V2=obj)
    elif request.method == 'GET':
        print('from get !!')
        return render_template('moore.html')

@app.route("/meta1.html",methods=("GET","POST"))
def meta1():
    if request.method == 'POST':
        fl = request.files['file']
        lst = fl.stream.readlines()
        numberofele = int(lst[0])
        processTime = lst[1].decode('utf-8').split('\t')
        dueDate = lst[2].decode('utf-8').split('\t')
        jobs = [i + 1 for i in range(numberofele)]
        p = [int(i) for i in processTime]
        d = [int(i) for i in dueDate]
        data = [[jobs[i], p[i], d[i]] for i in range(len(jobs))]
        print(data)


        x_improved = RVNS(data,5)
        sequence2, obj = GVNS(x_improved,10)
        print("this is gvns", sequence2, obj)
        return render_template('meta1.html', v1=sequence2, v2=obj)
    elif request.method == 'GET':
        print('from get !!')
        return render_template('meta1.html')


    return render_template("meta1.html")
@app.route("/meta2.html",methods=("GET","POST"))
def meta2():
    if request.method == 'POST':
        fl = request.files['file']
        lst = fl.stream.readlines()
        numberofele = int(lst[0])
        processTime = lst[1].decode('utf-8').split('\t')
        dueDate = lst[2].decode('utf-8').split('\t')
        jobs = [i + 1 for i in range(numberofele)]
        p = [int(i) for i in processTime]
        d = [int(i) for i in dueDate]
        alpha = lst[3].decode('utf-8').split('\t')
        beta = lst[4].decode('utf-8').split('\t')
        alp= [int(i) for i in alpha]
        bet = [int(i) for i in beta]

        data = [[jobs[i], p[i], d[i],alp[i],bet[i]] for i in range(len(jobs))]
        print(data)


        x_improved = RVNS2(data,5)
        sequence2, obj = GVNS2(x_improved,10)
        print("this is gvns", sequence2, obj)
        return render_template('meta2.html', v1=sequence2, v2=obj)
    elif request.method == 'GET':
        print('from get !!')
        return render_template('meta2.html')


    return render_template("meta2.html")


if __name__== "__main__":
    app.run(host='0.0.0.0')
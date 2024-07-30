from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/Krishna')
def krishna():
   return render_template('index.html')

@app.route('/Krishna1')
def krishna1():
   return render_template('ind1.html')


@app.route('/Krishna2')
def krishna2():
   return render_template('ind2.html')

@app.route('/Krishna3')
def krishna3():
   return render_template('index.html')

@app.route('/Krishna4')
def krishna4():
   return render_template('ind3.html')

@app.route('/Krishna5')
def krishna5():
   return render_template('ind4.html')

@app.route('/Krishna6')
def krishna6():
   return render_template('ind5.html')

@app.route('/Krishna7')
def krishna7():
   return render_template('ind6.html')

@app.route('/Krishna10')
def krishna10():
   return render_template('ind10.html')


if __name__=="__main__":
   app.run(debug=True)
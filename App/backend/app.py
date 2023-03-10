from flask import Flask, render_template

app=Flask(__name__,template_folder='../front-end/templates',static_folder='../front-end/static')

@app.route("/")
def start():
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)
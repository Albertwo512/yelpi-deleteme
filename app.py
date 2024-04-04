from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def index():
    return render_template('base.html',location=request.form.get['location',None])

    


if __name__ == '__main__':
    app.run(debug=True)

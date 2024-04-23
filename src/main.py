# from flask import Flask, render_template
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def index():
#     return render_template('webpage.html')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def index():
    return render_template('webpage.html')

if __name__ == '__main__':
    app.run(debug=True)

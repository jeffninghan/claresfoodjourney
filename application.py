from flask import Flask, render_template
application = Flask(__name__)
 
@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', user_image='/static/funny_clare.png')
 
if __name__ == '__main__':
    application.run()

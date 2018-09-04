import subprocess

from flask import Flask, render_template

application = Flask(__name__)
 
@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', user_image='/static/funny_clare.png')


@application.route('/status')
def status():
  status = subprocess.check_output(['bash','-c', "awk '/./{line=$0} END{print line}' /home/ec2-user/instagram/claresfoodjourney.log"])
  return render_template('status.html', status=status)

 
if __name__ == '__main__':
    application.run()

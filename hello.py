from flask import Flask, render_template
from flask_script import Manager
from flask_bootstrap import Bootstrap
from downloader.db_function import DBSession
from downloader.models import Qingsongyike

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qsyk')
def qsyk():
    session = DBSession()
    qingsongyike = session.query(Qingsongyike).first()
    session.close()
    title=qingsongyike.title
    body=qingsongyike.body
    return render_template('qsyk.html',title=title, body=body)


if __name__ == '__main__':
    manager.run()
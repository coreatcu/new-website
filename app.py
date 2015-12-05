from flask import Flask, render_template
from eventum import Eventum

app = Flask(__name__)
app.config.from_object('config.flask_config')

eventum = Eventum(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/event/<slug>')
def view_event(slug):
    return slug


@app.route('/event/<slug>/<index>')
def view_rec_event(slug, index):
    return '{} #{}'.format(slug, index)

if __name__ == '__main__':
    app.run(host=app.config['HOST'], port=app.config['PORT'])

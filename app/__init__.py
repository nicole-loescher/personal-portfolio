from flask import Flask, render_template
from .forms import ContactForm
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def home():
    form = ContactForm()
    return render_template('index.html', form=form)


@app.route('/', methods=['POST'])
def contact():
    form = ContactForm()
    return render_template('index.html', form=form)

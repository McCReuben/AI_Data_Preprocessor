import json
import os
import pickle
import random
import secrets

import pandas
from flask import (Flask, flash, redirect, render_template, request, session,
                   url_for)
from flask_wtf import FlaskForm, Form
from sklearn import preprocessing
from wtforms import FileField

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)


@app.route('/upload')
def upload():
    form = DataForm()
    return render_template('upload.html', form=form)

class DataForm(FlaskForm):
    data = FileField('Data File')

@app.route('/preprocess', methods=['POST'])
def preprocess():
    form = DataForm()
    if form.validate_on_submit():
        # Get the file from the form
        file = request.files['data']
        
        # Preprocess the file here
        # You can use any library or method you like to preprocess the data
        
        # Return a response to the user
        return 'Data preprocessed!'
    return 'An error occurred!'

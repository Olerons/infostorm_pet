# -*- coding: utf-8 -*-
from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user={'username': "noname"})

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Its OK')
        return redirect('/index')
    return render_template('login.html', title="Вход", form=form)
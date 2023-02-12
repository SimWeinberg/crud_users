from flask import Flask, render_template, request, redirect

from flask_app.models.user import User

app = Flask(__name__)
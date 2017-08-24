from flask import Flask

app = Flask(__name__)
from app import views
from app import login
from app import register
from app import remove

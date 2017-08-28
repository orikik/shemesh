from flask import Flask

app = Flask(__name__)
from app import views
from app import login
from app import register
from app import remove
from app import logout
from app import update



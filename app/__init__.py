from flask import Flask

app = Flask(__name__)

from app import views
from app import login
from app import registration
from app import remove
from app import logout
from app import update
from app import file_upload
from app import file_deleting
from app import file_update
from app import file_get
from app import directory_new
from app import directory_change_name
from app import directory_remove
from app import directory_getNameFiles

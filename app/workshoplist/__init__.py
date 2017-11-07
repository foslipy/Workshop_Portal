# app/admin/__init__.py

from flask import Blueprint

workshoplist = Blueprint('workshoplist', __name__)

from . import views

#定义蓝图
from flask import Blueprint
bp = Blueprint('api', __name__)

from app.api import ping

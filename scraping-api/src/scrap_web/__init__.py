from flask import Blueprint

scrap_web = Blueprint("scrap_web", __name__, url_prefix="/api/scrap-web")

from src.scrap_web import routes
from flask import Flask
from flask_cors import CORS

def create_app():
  app = Flask(__name__)
  CORS(app, resources={r"/*": {"origins": ["http://localhost:5173"]}})

  # Set mode
  mode = 'dev'

  # Load config
  if mode == 'prod':
    app.config.from_object('config.ProductionConfig')
  else:
    app.config.from_object('config.DevelopmentConfig')

  # Call Blueprints
  from src.scrap_web import scrap_web

  # Load Blueprints
  app.register_blueprint(scrap_web)

  return app, mode


if __name__ == '__main__':
  create_app()
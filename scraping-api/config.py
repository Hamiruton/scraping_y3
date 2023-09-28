import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
  DEBUG=False
  TESTING=False
  SECRET_KEY="i_love_you"


class ProductionConfig(Config):
  ENV='production'
  SECRET_KEY=os.getenv('SECRET_KEY')


class DevelopmentConfig(Config):
  DEBUG=True
  ENV='development'

  SECRET_KEY="i_love_you"
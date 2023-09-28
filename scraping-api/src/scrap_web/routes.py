""" Import module """
from src.scrap_web import scrap_web
from flask import request, jsonify, make_response
import json
from src.utils.async_scrap import main2

@scrap_web.get('/')
def test():
  return make_response(jsonify({"Response": "Test"}), 200)


@scrap_web.post('/url')
def test_url():
  data = request.get_json()
  print(data)
  mail_sent = main2(data['urlSent'], limit=int(data['limit']))
  return make_response(jsonify({"Response": {"extraction": True, "mail": mail_sent}}), 200)
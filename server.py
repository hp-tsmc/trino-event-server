from flask import Flask, json, request
import logging

from matplotlib.font_manager import json_dump

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)

app = Flask(__name__)

@app.route('/logs', methods=['POST'])
def parse_event():
  requestJson = request.get_json()
  logging.debug(json.dumps(requestJson))

  logging.info("user is " + requestJson['context']['user'] + " queryState: " + requestJson['metadata']['queryState'])

  if requestJson['metadata']['queryState'] == "QUEUED":
    print("parse QUEUED event")
    
  elif requestJson['metadata']['queryState'] == "FINISHED":
    print("parse FINISHED event")
  elif requestJson['metadata']['queryState'] == "FAILED":
    print("parse FAILED event")
  else:
    logging.warning("Receiving unknown body: " + json.dumps(requestJson))

  return "OK"

if __name__ == '__main__':
  app.run(host= '0.0.0.0',debug=True)
import time

from flask import Flask, escape, request

app = Flask(__name__)

start_time = time.time()
should_shutdown = False

@app.route('/liveness')
def liveness():
  global should_shutdown
  if not should_shutdown:
    return "OK"
  else:
    return "NOK", 404

@app.route('/readiness')
def readiness():
  global start_time
  if time.time() - start_time > 30:
    return "OK"
  return "NOK", 404

@app.route('/')
def hello():
  name = request.args.get("name", "World")
  return 'Hello!'

@app.route('/shutdown')
def shutdown():
  global should_shutdown
  should_shutdown = True
  return "Done"

@app.route('/chew_memory')
def chew_memory():
  some_str = ' ' * 512000000
  return some_str

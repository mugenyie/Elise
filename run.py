# /run.py
import os

from src.app import create_app

if __name__ == '__main__':
  env_name = os.getenv('FLASK_ENV')
  app = create_app(env_name)
  app.run()




# Run a test server.
# from src import app
# app.run(host='127.0.0.1', port=8080, debug=True)
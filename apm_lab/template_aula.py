import os
import psycopg
from flask import Flask, render_template, request
from dotenv import load_dotenv
from elasticapm.contrib.flask import ElasticAPM
import logging
load_dotenv()
app = Flask(__name__)
logging.basicConfig(filename='flask.log', level=logging.DEBUG, format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


app.config['ELASTIC_APM'] = {

  'SERVICE_NAME': 'app_flask',


  'SECRET_TOKEN': '',
  'DEBUG': True,

# # # Set the custom APM Server URL (default: http://localhost:8200)
  'SERVER_URL': 'http://localhost:8200',

# # # Set the service environment
  'ENVIRONMENT': 'dev',
  }

apm = ElasticAPM(app)
@app.route("/")
def hello_world():
    try:
        conexao = psycopg.connect(host=os.environ['DATABASE_HOST'],
            dbname=os.environ['DATABASE_NAME'],
            user=os.environ['DATABASE_USER'],
            port=os.environ['DATABASE_PORT'],
            password=os.environ['DATABASE_PASS'],)
        test_db="e Banco conectado com sucesso    "
        get_command_linux = os.popen('hostname')
        d_command = get_command_linux.read()
        d_result = d_command + test_db
        return render_template('index.html', d_output=d_result)
    except Exception as err:
        
        app.logger.critical(err)
        return render_template('erro.html', d_output=err)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)

import os
from ossaudiodev import error
import psycopg

from flask import Flask, render_template, request
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
 

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
        app.logger.info('Info level log')
        return render_template('index.html', d_output=d_result)
    except Exception as err:
        err_test_db=" FALHA "
        get_command_linux = os.popen('hostname')
        d_command = get_command_linux.read()
        d_result = d_command + err_test_db
        
        return render_template('erro.html', d_output=d_result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = False)


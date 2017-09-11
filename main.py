import flask
import json
import os
from flask import request,g
import glob 
import sqlite3

from flask import Flask
from flask import render_template

app = Flask(__name__)

# curl -X POST -F fileup=@/var/log/wifi.log -F filename=wifi.log -F jobid=1 -F hostname=macbook1 http://localhost:9090/upload
# curl -s http://localhost:9090/client/download  | /bin/bash
# insert into q values (0, 'Matts-MacBook-Pro-3.local','/var/log/wifi.log',1);
# insert into q values (null, 'salt-dal-01.prd.inteliquent.net','/var/log/salt/minion',2);
# insert into q values (null, 'salt-dal-01.prd.inteliquent.net','/var/log/salt/master',2);

@app.route("/client/download")
def downloadScript():
    return render_template("./client.sh", serverUrl=request.url_root)


@app.route("/client/jobs/<hostname>")
def getJobs(hostname):
    db = get_db()
    logList = []
    for jobs in db.execute("select * from q where hostname='%s'" % hostname):
        logList.append( str(jobs[2]) + ":"  + str(jobs[3]) )

    return "logs=(%s)\n" % " ".join(logList)


@app.route("/upload", methods=['POST'])
def uploadFile():
   
    
    projectID = request.form['projectID']
    inputLog  = request.files['fileup']
    filename  = request.form['filename']
    hostname  = request.form['hostname']
    directory = "./logs/%s/" % (projectID)
    
    if not os.path.exists( directory):
        os.makedirs( directory)

    inputLog.save( directory + hostname + "_" + filename)

    return ""

@app.route("/")
def default():
    return render_template("index.html")

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect('q.db')
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

if __name__ == "__main__":

    if not os.path.exists("q.db"):
        db = sqlite3.connect('q.db')
        db.execute("CREATE TABLE IF NOT EXISTS q(id INTEGER PRIMARY KEY AUTOINCREMENT, hostname text, filepath text, projectID int)")
        db.commit() 
        db.close()

    appHost = int(os.environ['APP_HOST']) if 'APP_HOST' in os.environ else '0.0.0.0'
    appPort = int(os.environ['APP_PORT']) if 'APP_PORT' in os.environ else 9090
    app.run(debug=True, host=appHost,port=appPort)

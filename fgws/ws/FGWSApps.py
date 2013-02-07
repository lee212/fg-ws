import os
from flask import Flask, jsonify
import json
from FGMySQLDB import FGMySQLDB
from FGMimerender import mimerender

app = Flask(__name__)

@app.route("/get_active_users.json")
@mimerender
def get_active_users():
    userids = get_active_username()
    res = convert_username(userids)
    return {"message": res}

def get_active_username():
    mdb = FGMySQLDB()
    mdb.dbinfo(os.environ["FG_OPENSTACK_DB_HOST"], os.environ["FG_OPENSTACK_DB_ID"], os.environ["FG_OPENSTACK_DB_PASS"], os.environ["FG_OPENSTACK_DB_NAME"])
    #mdb.dbinfo("hostname","id","pass","db")
    mdb.connect()
    res = mdb.select("select distinct name from keystone.user, (select user_id from instances where vm_state='active' and task_state is null) as a where id=a.user_id")
    mdb.close()
    return res

def convert_username(userids):
    res = []
    mdb = FGMySQLDB()
    mdb.dbinfo(os.environ["FG_METRIC_DB_HOST"], os.environ["FG_METRIC_DB_ID"], os.environ["FG_METRIC_DB_PASS"], os.environ["FG_METRIC_DB_NAME"])
    #mdb.dbinfo("hostname","id","pass","db")
    mdb.connect()
    for record in userids:
        name = mdb.select("select first_name, last_name, email from userinfo where username='%s' limit 1" % record["name"])
        try:
            name = name[0]
            name["ownerid"] = record["name"]
            res.append(name)
        except:
            pass
    mdb.close()
    return res

if __name__ == "__main__":
    app.run(host=os.environ["FG_HOSTING_IP"], debug=True)
    #app.run(host="0.0.0.0", debug=True)

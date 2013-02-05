from flask import Flask, jsonify
import json
import mimerender
from FGMySQLDB import FGMySQLDB

mimerender = mimerender.FlaskMimeRender()

render_xml = lambda message: '<message>%s</message>' % str(message)
render_json = lambda **args: jsonify(args)
render_html = lambda message: '<html><body>%s</body></html>' % str(message)
render_txt = lambda message: message

app = Flask(__name__)

@app.route("/get_active_users.json")
@mimerender(
        default = 'json',
        html = render_html,
        xml  = render_xml,
        json = render_json,
        txt  = render_txt
        )
def get_active_users():
    userids = get_active_username()
    res = convert_username(userids)
    return {"message": res}

def get_active_username():
    mdb = FGMySQLDB()
    #mdb.dbinfo("hostname","id","pass","db")
    mdb.connect()
    res = mdb.select("select distinct name from keystone.user, (select user_id from instances where vm_state='active') as a where id=a.user_id")
    mdb.close()
    return res

def convert_username(userids):
    res = []
    mdb = FGMySQLDB()
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
    #app.run(host="0.0.0.0", debug=True)

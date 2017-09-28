import pyodbc
from flask import Flask, render_template, request, session, abort, flash, redirect, url_for
import os
from passlib.hash import sha256_crypt
app = Flask(__name__)

password = sha256_crypt.encrypt("password")
password2 = sha256_crypt.encrypt("password")


con_string = """driver=ODBC Driver 13 for SQL Server;server=choicemis.choice.co.th;
                                                database=choicemis;
                                                uid=choicemis;
                                                pwd=choicemis711"""



@app.route('/home')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('home.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.method == "POST":
        try:
            if request.form['password'] == 'choice711' and request.form['username'] == 'choice':
                session['logged_in'] = True
            else:
                flash('wrong password!')
            return home()
        except :
            error = "Invalid credentials, try again."
            return render_template("login.html", error=error)


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/case')
def case():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('case.html')


@app.route('/offen')
def offen():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('offen.html')


@app.route('/follow')
def follow():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("follow.html")


@app.route('/update')
def update():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('updatefoll.html')

@app.route('/testform')
def testform():
   return render_template('testform.html')

@app.route('/addcase', methods=['POST', 'GET'])
def addcase():
    if request.method == 'POST':
        try:
            bcode = request.form['bcode']
            bname = request.form['bname']
            date = request.form['date']
            cinout = request.form['cinout']
            ctype = request.form['ctype']
            cost = request.form['cost']
            respons = request.form['respons']
            edate = request.form['edate']
            detail = request.form['detail']
            notification = request.form['notification']

            with pyodbc.connect(con_string) as con:

                cur = con.cursor()

                cur.execute("""insert into casedemo(bcode,bname,sdate,cinout,ctype,cost,respons,edate,detail,notification) 
        values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",(bcode,bname,date,cinout,ctype,cost,respons,edate,detail,notification) )

                cur.execute("""select caseid from casedemo 
                                order by caseid desc""")
                idc = cur.fetchone()[0];

                con.commit()
                msg = "Case Successfully Added"

        except:
            con.rollback()
            msg = "error in insert operation"
        finally:
            return render_template("offen.html", msg=msg, idc=idc)
            con.close()

@app.route('/addoffen', methods=['POST', 'GET'])
def addoffen():
    if request.method == 'POST':
        try:

            caseid = request.form['caseid']
            ofname = request.form['ofname']
            id = request.form['id']
            position = request.form['position']
            month = request.form['month']
            year = request.form['year']
            # worktime = request.form['worktime']

            with pyodbc.connect(con_string) as con:

                cur = con.cursor()

                cur.execute("""insert into offendemo(caseid,ofname,id,position,month,year) 
        values(?, ?, ?, ?, ?, ?)""",(caseid,ofname,id,position,month,year) )

                cur.execute("""select caseid from casedemo
                                                order by caseid desc""")
                idc = cur.fetchone()[0];
                con.commit()
                msg = "Offensive Successfully Added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("offen.html", msg=msg, idc=idc)
            con.close()

@app.route('/addoffenfoll', methods=['POST', 'GET'])
def addoffenfoll():
    if request.method == 'POST':
        try:

            caseid = request.form['caseid']
            ofname = request.form['ofname']
            id = request.form['id']
            position = request.form['position']
            month = request.form['month']
            year = request.form['year']
            # worktime = request.form['worktime']

            with pyodbc.connect(con_string) as con:

                cur = con.cursor()

                cur.execute("""insert into offendemo(caseid,ofname,id,position,month,year) 
        values(?, ?, ?, ?, ?, ?)""",(caseid,ofname,id,position,month,year) )

                cur.execute("""select caseid from casedemo
                                                order by caseid desc""")
                idc = cur.fetchone()[0];
                con.commit()
                msg = "Offensive Successfully Added"

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("offencomp.html", msg=msg, )
            con.close()

@app.route('/addfoll', methods=['POST', 'GET'])
def addfoll():
    if request.method == 'POST':
        try:

            caseid = request.form['caseid']
            foll_status = request.form['foll_status']
            foll_type = request.form['foll_type']
            foll_detail = request.form['foll_detail']
            datestatus = request.form['datestatus']
            # datetype = request.form['datetype']

            with pyodbc.connect(con_string) as con:

                cur = con.cursor()

                cur.execute("""insert into followdemo(caseid,foll_status,foll_type,foll_detail,datestatus) 
        values(?, ?, ?, ?, ?)""",(caseid,foll_status,foll_type,foll_detail,datestatus,))

                con.commit()
                msg = "Record successfully added"
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("comp.html", msg=msg)
            con.close()

@app.route('/updatefoll', methods=['POST', 'GET'])
def updatefoll():
    if request.method == 'POST':
        try:

            caseid = request.form['caseid']
            datestatus = request.form['datestatus']
            datetype = request.form['datetype']
            foll_status = request.form['foll_status']
            foll_type = request.form['foll_type']
            foll_detail = request.form['foll_detail']

            with pyodbc.connect(con_string) as con:

                cur = con.cursor()

                cur.execute("""update followdemo 
                set foll_status=?, foll_type=?, foll_detail=?, datestatus=?, datetype=?
                WHERE caseid=? 
                """,(foll_status,foll_type,foll_detail,datestatus,datetype,caseid) )

                con.commit()
                msg = "Record successfully UPDATED"
        except:
            con.rollback()
            msg = "error in update operation"

        finally:
            return render_template("offen.html", msg=msg)
            con.close()

@app.route('/showdata')
def list():
    with pyodbc.connect(con_string) as con:

            cur = con.cursor()

            cur.execute("select * from casedemo")

            rows = cur.fetchall();
            return render_template("showdata.html", rows=rows)

@app.route('/showof')
def showof():
    with pyodbc.connect(con_string) as con:

            cur = con.cursor()

            cur.execute("select * from offendemo")

            rows = cur.fetchall();
            return render_template("showof.html", rows=rows)

@app.route('/showfoll')
def showfoll():
    with pyodbc.connect(con_string) as con:

            cur = con.cursor()

            cur.execute("select * from followdemo")

            rows = cur.fetchall();
            return render_template("showfoll.html", rows=rows)

@app.route('/join')
def join():
    with pyodbc.connect(con_string) as con:

            cur = con.cursor()

            cur.execute("""select * from casedemo a 
            INNER JOIN offendemo b on a.caseid = b.caseid 
            INNER JOIN followdemo c on a.caseid = c.caseid
            """)

            rows = cur.fetchall();
            return render_template("join.html", rows=rows)

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True)

# INNER JOIN followdemo c on a.caseid = c.caseid
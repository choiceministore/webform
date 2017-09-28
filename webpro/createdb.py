import pyodbc

con_string = """driver=ODBC Driver 13 for SQL Server;server=choicemis.choice.co.th;
                                                database=choicemis;
                                                uid=choicemis;
                                                pwd=choicemis711"""

# def create_table2():
#     sql = """
#         create table offendemo(
#             offenid int IDENTITY(1,1) PRIMARY KEY,
#             caseid int FOREIGN KEY REFERENCES casedemo(caseid),
#             ofname varchar(255) NOT NULL,
#             id int NOT NULL,
#             position varchar(255) NOT NULL,
#             worktime varchar(255),
#
#         )
#     """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql)

def create_table3():
    sql = """
        create table followdemo(
            follid int IDENTITY(1,1) PRIMARY KEY,
            caseid int FOREIGN KEY REFERENCES casedemo(caseid),
            foll_status varchar(255) NOT NULL,
            foll_type varchar(255) NOT NULL,
            foll_detail varchar(255),

        )
    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

# def create_table1():
#     sql = """
#         create table casedemo(
#             caseid int IDENTITY(1,1) PRIMARY KEY,
#             bcode int NOT NULL,
#             bname varchar(255),
#             sdate text,
#             cinout varchar(255) NOT NULL,
#             ctype varchar(255) NOT NULL,
#             cost int,
#             respons varchar(255) NOT NULL,
#             edate text,
#             detail text,
#             notification varchar(255) NOT NULL
#         )
#     """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql)

# def insert_demo2():
#     sql = """
#         insert into offendemo(caseid,ofname,id,position,worktime)
#         values('')
#                 """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql)

def insert_demo1():
    sql = """
        insert into casedemo(bcode,bname,sdate,cinout,ctype,cost,respons,edate,detail,notification)
        values('9219', 'chaingmai land', '16/10/2560', 'test', 'test', 100000,
                'test', '16/10/2560', 'test', 'test')
    """
#     with pyodbc.connect(con_string) as con:
#         con.execute(sql)
#
# def select_demo():
#     sql = """
#             select *
#             from casedemo
#             """
#     with pyodbc.connect(con_string) as con:
#         for row in con.execute(sql):
#             print(row)

def alter_table():
    sql = """
        ALTER TABLE followdemo
        ADD datetype text
                 
    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)


def create_table4():
    sql = """
        create table gentest(
            genid int IDENTITY(20170001,1) PRIMARY KEY,
            name varchar(255)
       )
    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

def insert_table4():
    sql = """
        insert into gentest(name) values('best')
       
    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

def select_table4():
    sql = """
        select * from gentest
       
    """
    with pyodbc.connect(con_string) as con:
        for row in con.execute(sql):
            print(row)


def select_sc():
    sql = """
        
        select * from INFORMATION_SCHEMA.COLUMNS 
        where TABLE_NAME='offendemo'

    """
    with pyodbc.connect(con_string) as con:
        for row in con.execute(sql):
            print(row)


def insert_offen():
    sql = """

        insert into offendemo(caseid,ofname,id,position,worktime) values('18','best','12345','employee','20')

    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

def alter_offen():
    sql = """

        ALTER TABLE offendemo 
        ALTER COLUMN id text

    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)

def alter_worktime():
    sql = """

        ALTER TABLE offendemo 
        ADD year text

    """
    with pyodbc.connect(con_string) as con:
        con.execute(sql)




if __name__ == '__main__':
    # create_table4()
    # insert_table4()
    # alter_offen()
    alter_worktime()
    # create_table3()
    # alter_table2()
    # insert_demo3()
    # select_demo()
    # select_demo2(['F', 50])
    # insert_demo2(['M', 70, 170])
    # for _ in range(10):
    #     g = random.choice('MF')
    #     w = random.normalvariate(55, 6)
    #     h = random.normalvariate(160, 7)
    #     insert_demo2([g, w, h])
    # update_demo('F')
    # h = float(input("height: "))
    # g = input("M or F: ")
    # delete_demo([h, g])
    # select_demo()
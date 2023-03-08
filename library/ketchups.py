import bcrypt
import MySQLdb
import sshtunnel


# password=b'texttest'

# sel = bcrypt.gensalt()

# with open("/root/saltpepperketchup/outputs/sel.txt", "wb") as binary_file:
   
# #     # Write bytes to file
#      binary_file.write(sel)

# ketchup = bcrypt.hashpw(password, sel)


def a():

    ssh_username = 'allospphtests'
    ssh_password = 'r1g0l0p4ssw0rd'
    user = 'allosddpysstes'
    passwd = 'r1g0l01234'
    host = '127.0.0.1'
    port = '12345'
    db = 'allosdpyssdefault'

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.mypythonanywhere.com'),
        ssh_username=ssh_username, ssh_password=ssh_password,
        remote_bind_address=('allosdpyth.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user=user,
            passwd=passwd,
            host=host, port=tunnel.local_bind_port,
            db=db,
        )
        # Do stuff
        cursor = connection.cursor()

        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            dd = d.encode('utf8')
            cursor.close()
            connection.close()

    password = dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
        sel = binary_file.read()

    ketchup = bcrypt.hashpw(password, sel)

    return ketchup


def b():

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='johndoe', ssh_password='pass123!',
        remote_bind_address=('example.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='johnnydoe',
            passwd='mypassword123',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='mydatabase',
        )
        # Do stuff
        cursor = connection.cursor()

        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            dd=d.encode('utf8')

            cursor.close()    
            connection.close()

    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
        sel=binary_file.read()

    ketchup = bcrypt.hashpw(password, sel)

    return ketchup


def c():
    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosy3onsstost', ssh_password='gcs321%$',
        remote_bind_address=('allosygyts.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allo2egytses',
            passwd='motsore_4m3p',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allosyxonssdefault',
        )
        # Do stuff
        cursor = connection.cursor()

        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            dd = d.encode('utf8')
            cursor.close()
            connection.close()

    password = dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
        sel = binary_file.read()

    ketchup = bcrypt.hashpw(password, sel)

    return ketchup


def d():
    import random
    import string
    import bcrypt
    import MySQLdb
    import sshtunnel
    
    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='peterlui7', ssh_password='jkhfd7JH%#d',
        remote_bind_address=('allospytst.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospyddfdes', 
            passwd='dipgla212&^_',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythcdult',
        )
        cursor = connection.cursor()

        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            dd=d.encode('utf8')
            cursor.close() 
            connection.close()

    password = dd
    with open("/root/ketchuppepper/salt.txt", "rb") as binary_file:
        salt = binary_file.read()

    ketchup = bcrypt.hashpw(password, salt)

    return ketchup


def e():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythonsstests', ssh_password='0043b3$$',
        remote_bind_address=('allospythts.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospysddsstes',
            passwd='rigolo1234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythedlt',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup


def f():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosfefefests', ssh_password='00ef$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allovrffvctes',
            passwd='allwdwdwd4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythfeffe$$ult',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def g():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospyrvfe3efefts', ssh_password='00003rr3r3r3',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allosfrfres',
            passwd='allo13eedd',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def h():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythonsts', ssh_password='00effefe3$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospytefftes',
            passwd='allefeffeef4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def i():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythests', ssh_password='07efef$$',
        remote_bind_address=('allospythestests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospytstes',
            passwd='aeffe234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def j():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythsstseests', ssh_password='07ef!hdn3$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='al3stes',
            passwd='aeffedd234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='alpyt3e$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def k():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='all2333ests', ssh_password='07223$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospee2ees',
            passwd='aefe2e3234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def l():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosped3w3tests', ssh_password='07efe12eh3r3r$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allosrd3e3tes',
            passwd='aefd3rf3rd34',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def m():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospy3deerfetests', ssh_password='07efotherr3',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allos3efrr3es',
            passwd='aee33re3dr4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def n():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='al3rdff3sts', ssh_password='07ef3r3rr33r3r$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='arealfs',
            passwd='ae2333hr3r4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def o():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospytfeef3ests', ssh_password='0ff0011$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='addeees',
            passwd='aeffedde234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def p():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospytngejfts', ssh_password='07eftess$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allosrainbowstes',
            passwd='aeffepartter',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def q():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospsaluttestests', ssh_password='07ddalutttfef$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allosppistas',
            passwd='fashionaa222',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def r():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythorgrftests', ssh_password='bitterrun$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='ffjrff',
            passwd='biteher233',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def s():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosrealogstests', ssh_password='07rrefrfr$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='tester',
            passwd='ddacddtrap',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def t():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosalutpython', ssh_password='refref22$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospr3tes',
            passwd='asalut234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def u():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allosallolttests', ssh_password='07saluttt2f$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allosseeytstes',
            passwd='aefftest4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def v():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospy2eee2estests', ssh_password='07efefee3f$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='alsaluspytstes',
            passwd='englishe122',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def w():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allofefeffthonsstests', ssh_password='07e222!!$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='alleffetstes',
            passwd='aeff3rf334',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def x():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospresstests', ssh_password='07ef2e2e$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allospy3ee11pythontstes',
            passwd='aeffeede3e3e3e234',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def y():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospythonsstests', ssh_password='07efrffrf$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='allofrfrfes',
            passwd='aefewd323e4',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

def z():


    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='allospd3d3edests', ssh_password='07efed2dee2$$',
        remote_bind_address=('allospythonsstests.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='alldsalutes',
            passwd='aeff122secr34',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='allospythonsstes$default',
        )
        # Do stuff
        cursor = connection.cursor()


        cursor.execute("SELECT passw from table")
        for d in cursor.fetchone():
            #print("ketchup success")
            dd=d.encode('utf8')

            cursor.close()
                    
            connection.close()


    password=dd

    with open("/root/saltpepperketchup/outputs/sel.txt", "rb") as binary_file:
    
    #     # Write bytes to file
        sel=binary_file.read()


    ketchup = bcrypt.hashpw(password, sel)


    return ketchup

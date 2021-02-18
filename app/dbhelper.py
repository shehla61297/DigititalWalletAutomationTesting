import psycopg2
# from app.config import config
import config


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.config()

        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def create_tables():
    commands = (
        """
        Create Table UserStatus
            (
            ID SERIAL PRIMARY KEY,
            UserUUID VARCHAR(200),
            RelationshipID VarChar(100)	,
            StatusID INT,
            Created_Date Date
            )	
        """,
        """ 	
        Create Table StatusMaster
        (
        ID SERIAL PRIMARY KEY,
        StatusCode CHAR(50),
        StatusDetails VarChar(200),
        Created_Date Date,
        IsActive Boolean	
        )
        """)

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_data():
    commands = (
        """
        INSERT INTO UserStatus
            (
            UserUUID VARCHAR(200),
            RelationshipID VarChar(100)	,
            StatusID INT,
            Created_Date Date
            )	
        """,
        """ 	
        Create Table StatusMaster
        (
        ID SERIAL PRIMARY KEY,
        StatusCode CHAR(50),
        StatusDetails VarChar(200),
        Created_Date Date,
        IsActive BIT	
        )
        """)

    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def get_user_status_by_uuid(user_uuid):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config.config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()
        query = "select StatusMasterV1.StatusCode from UserStatusV1 inner " \
                "join StatusMasterV1 on UserStatusV1.StatusID = StatusMasterV1.StatusID and UserStatusV1.useruuid = '" + user_uuid + "'" \
                                                                                                                                     "order by UserStatusV1.userstatussn desc Limit 1 "

        cur.execute(str(query))

        print("The number of parts: ", cur.rowcount)
        user_data = cur.fetchmany()
        user_status_code = None

        for row in user_data:
            user_status_code = row[0].strip()

        # close the communication with the PostgreSQL
        cur.close()
        return user_status_code
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')


def insert_userstatus(user_uuid, relationshipdid):
    conn = None
    IsInserted = 0
    try:
        # read connection parameters
        params = config.config()
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()

        query = " insert into userstatus(useruuid,relationshipid,statusid ,created_date) values('" + user_uuid + "','" + relationshipdid + "'" + ",1, Now() )"
        print(query)
        cur.execute(str(query))

        conn.commit()
        # close the communication with the PostgreSQL
        cur.close()
        return IsInserted
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return IsInserted


def update_userstatus(user_uuid, relationshipdid, statusid):
    conn = None
    IsUpdated = 0
    try:
        # read connection parameters
        params = config.config()
        conn = psycopg2.connect(**params)
        # create a cursor
        cur = conn.cursor()
        query = " update userstatus   SET StatusID = " + statusid + "  where useruuid = '" + user_uuid + "' and relationshipid = '" + relationshipdid + "'"
        print(str(query))
        cur.execute(str(query))

        conn.commit()
        # close the communication with the PostgreSQL
        cur.close()
        return IsUpdated
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
        return IsUpdated
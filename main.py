import pyodbc

def main():


    Query = 'SELECT * FROM PulseInterface202_8260.dbo.Stores'
    Server = '192.168.80.5'
    Database = 'PulseInterface202_8260'
    UserID = 'sa'
    Password = 'dpksa@456'
    TimeOut = 60

    # ConnectionString
    ConnString = 'DRIVER={ODBC Driver 11 for SQL Server};SERVER=' + Server + ';DATABASE=' + Database + ';UID=' + UserID + ';PWD=' + Password

    # Generate connection string
    Conn = pyodbc.connect(ConnString, timeout=TimeOut)

    # Create Cursor
    Cur = Conn.cursor()

    # Execute the query
    Cur.execute(Query)

    # Get the resultd
    Result = Cur.fetchall()

    # Delete cursor
    del Cur

    # Close Connection
    Conn.close()

    print(Result)

    return Result

main()

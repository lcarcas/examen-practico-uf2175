import mysql.connector


def connection_database(host, user, password, database):
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=int(3307)
    )

    return connection


def get_users(query,):
    results = (query, )
    return


def execute_query(query, ):
    cursor = connection.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


if __name__ == '__main__':
    conn =connection_database
    query = ""
    get_users(, conn)




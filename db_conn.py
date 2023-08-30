import psycopg2

try:
    conn = psycopg2.connect(user='postgres',
                            password='123456',
                            host='localhost',
                            port='5432',
                            database='Northwind')
    print('database connected successfully')

    cursor = conn.cursor()
    query = 'select * from products'

    cursor.execute(query)
    records = cursor.fetchall()
    for row in records:
        print(f'id: {row[0]} id: {row[1]} id: {row[5]}')
except:
    print('something went wrong!')


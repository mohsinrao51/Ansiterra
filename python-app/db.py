import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='terraform-20240715110217178900000004.cty20iusmhga.us-west-2.rds.amazonaws.com',
        user='admin',
        password='StrongPassword123!',
        database='mydb'
    )
    return connection

def create_visitors_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS visitors (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            visit_time DATETIME NOT NULL
        );
    ''')
    conn.commit()
    cursor.close()
    conn.close()


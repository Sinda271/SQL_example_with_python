import mysql.connector
from mysql.connector import errorcode

# ******************** Constants *****************************
CONFIG = {
    'user': 'Sinda',
    'password': 'Sonda25516122!',
    'host': '127.0.0.1',
    'database': 'walmart',
}
MODES = list(range(0, 4))

# ******************** Functions *****************************
def create_table(cursor):
    # Create WMsale table
    query = """CREATE TABLE IF NOT EXISTS WMsales (
	invoice_id  VARCHAR(30) NOT NULL PRIMARY KEY,
	branch  VARCHAR (5) NOT NULL,
    city VARCHAR (30) NOT NULL,
    customer_type VARCHAR (30) NOT NULL,
    gender  VARCHAR(10) NOT NULL,
    product_line VARCHAR (100) NOT NULL,
    unit_price  DECIMAL(10,2) NOT NULL,
    quantity INT NOT NULL,
    VAT  FLOAT(6,4) NOT NULL,
    total DECIMAL (12,4) NOT NULL,
    date DATETIME NOT NULL,
    time TIME NOT NULL,
    payment_method VARCHAR (15)  NOT NULL, 
    cogs  DECIMAL (10, 2) NOT NULL,
    gross_margin_pct FLOAT (11,9),
    gross_income DECIMAL(12, 4) NOT NULL,
    rating FLOAT (3, 1)
    )"""
    cursor.execute(query)
    
    # Check that WMsale table is created successfully
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
    
    # Fill table from csv file
    query = """
    LOAD DATA INFILE 'D:/PythonProjects/AssistanteEnseignement/semaine3/WalmartSalesData.csv' 
    INTO TABLE WMsales 
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n' 
    IGNORE 1 ROWS
    """
    cursor.execute(query)
    print("CSV data loaded successfully into table WMsales")
    
def select_table_info(cursor, mode):
    # Select all elements  
    if mode == 0: 
        cursor.execute('SELECT * FROM WMsales')
    # Select unique product lines 
    elif mode == 1:
        cursor.execute('SELECT DISTINCT product_line FROM WMsales')
    # Return Most selling product line
    elif mode == 2:
        cursor.execute(
            """SELECT product_line
            FROM WMsales
            GROUP BY product_line
            ORDER BY COUNT(*) DESC
            LIMIT 1
            """
        )
    # Return the revenue per month with descending order
    elif mode == 3:
        cursor.execute(
            """SELECT SUBSTRING(date, 6, 2) AS Month,
            SUM(total) AS Total_Revenue 
            FROM WMsales
            GROUP BY Month
            ORDER BY Total_Revenue DESC 
            """
        )
        
    results = cursor.fetchall()
    print(results)

# ******************** Main code *****************************
if __name__ == '__main__':
    try:
        cnx = mysql.connector.connect(**CONFIG)
        if cnx.is_connected():
            print("Connected successfully!")
            with cnx.cursor() as cursor:
                # Create table
                create_table(cursor)
                # Select info from table by passing mode index 
                select_table_info(cursor=cursor, mode=MODES[2])
                
        
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password or database name")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
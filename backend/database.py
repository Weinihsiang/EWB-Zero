import sqlite3

# @app.route('/new_user', methods=['POST'])
def add_user()->None:
    # # Get data from request
    # data = request.json
    
    # # Extract email details
    # user_email = data.get('user_email')
    # user_first_name = data.get('user_first_name')
    # user_last_name = data.get('user_last_name')

    """
    """
    conn, c = None, None
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()
        
        # Insert instances
        # many_users = [
        #     (0, 'John', 'Elder', 'john@codem.com'),
        #     (1, 'John', 'Elder', 'john@codem.com'),
        #     (2, 'John', 'Elder', 'john@codem.com')
        #     ]

        c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('John', 'Elder', 'john@codem.com'))
        c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('Alice', 'Elder', 'alice@codem.com'))
        c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('Emma', 'Elder', 'emma@codem.com'))
        #c.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?);", user_first_name, user_last_name, user_email)
        
        #c.execute("INSERT INTO producers VALUES (?,?,?);", many_customers)
        
        # # Display data
        # c.execute("""SELECT * FROM customers;""")
        # items = c.fetchall()
        # print(items)

        # c.execute("""SELECT * FROM producers;""")
        # suppliers = c.fetchall()
        # print(suppliers)

        conn.commit()

    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")

    finally:
        if c and not c.close:
            c.close()
        if conn and not conn.close:
            conn.close()


# @app.route('/new_product', methods=['POST'])
def add_product()->None:
    # # Get data from request
    # data = request.json
    
    # # Extract email details
    # user_id = data.get('user_id')
    # product_name = data.get('product_name')
    # amount = data.get('amount')
    # unit_price = data.get('unit_price')
    # product_addr = data.get('product_addr')
    """
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name text NOT NULL,
    amount INTEGER NOT NULL,
    price_per_unit REAL NOT NULL,
    product_address NOT NULL,
    user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE
    """
    conn, c = None, None
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()
        
        # Insert instances
        # many_products = [
        #     (0, 'Food1', 10, 11.1, '100 Queen Street', 0),
        #     (1, 'Food2', 20, 22.2, '200 King Avenue', 1),
        #     (2, 'Food3', 30, 33.3, '300 Cat Boulevard', 2)
        #     ]

        c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food1', 10, 11.1, '100 Queen Street', 1))
        c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food2', 20, 22.2, '200 King Avenue', 2))
        c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food3', 30, 33.3, '300 Cat Boulevard', 3))
        # c.execute("INSERT INTO customers VALUES (NULL, ?, ?, ?, ?, ?, ?);", product_name, amount, unit_price, product_addr, user_id)
        
        #c.execute("INSERT INTO producers VALUES (?,?,?);", many_customers)
        
        # # Display data
        # c.execute("""SELECT * FROM customers;""")
        # items = c.fetchall()
        # print(items)

        # c.execute("""SELECT * FROM producers;""")
        # suppliers = c.fetchall()
        # print(suppliers)

        conn.commit()

    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")

    finally:
        if c and not c.close:
            c.close()
        if conn and not conn.close:
            conn.close()

    
    



# def add() -> None:
#     """
#     """
#     conn, c = None, None
#     try:
#         # Connect to database
#         conn = sqlite3.connect('database.db')

#         # Create a cursor
#         c = conn.cursor()
        
#         # Insert instances
#         many_customers = [
#             ('0', 'John', 'Elder', 'john@codem.com'),
#             ('1', 'John', 'Elder', 'john@codem.com'),
#             ('2', 'John', 'Elder', 'john@codem.com')
#             ]

#         c.executemany("INSERT INTO customers VALUES (?,?,?,?);", many_customers)
#         c.execute("INSERT INTO producers VALUES (?,?,?);", many_customers)
        
#         # Display data
#         c.execute("""SELECT * FROM customers;""")
#         items = c.fetchall()
#         print(items)

#         c.execute("""SELECT * FROM producers;""")
#         suppliers = c.fetchall()
#         print(suppliers)

#         conn.commit()

#     except Exception as ex:
#         conn.rollback()
#         raise Exception(f"Couldn't set up environment for tests: \n{ex}")

#     finally:
#         if c and not c.closed:
#             c.close()
#         if conn and not conn.closed:
#             conn.close()
        
def update() -> None:
    """
    """
    conn, c = None, None
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()

        # Insert instances
        many_customers = [
            ('John', 'Elder', 'john@codem.com', '123'),
            ('John', 'Elder', 'john@codem.com', '456'),
            ('John', 'Elder', 'john@codem.com', '789')
            ]

        c.executemany("INSERT INTO customers VALUES (?,?,?,?)", many_customers)
        c.execute("INSERT INTO producers VALUES (?,?,?)", many_customers)
        
        # Display data
        c.execute("""SELECT * FROM customers""")
        items = c.fetchall()
        print(items)

        c.execute("""SELECT * FROM producers""")
        suppliers = c.fetchall()
        print(suppliers)

        conn.commit()

    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")

    finally:
        if c and not c.closed:
            c.close()
        if conn and not conn.closed:
            conn.close()
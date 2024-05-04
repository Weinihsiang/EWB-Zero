from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from database import add_user, add_product



# Initialize the Flask app
app = Flask(__name__)



# Define a route for the root URL
@app.route('/')
def index():
    return "Welcome to my Flask API agaerfddddddddfdadadadada!"

# Post Product function (Izabella)
@app.route('/new_user', methods=['POST'])
def add_user()->None:
    # Get data from request
    data = request.json
    
    # Extract email details
    user_email = data.get('user_email')
    user_first_name = data.get('user_first_name')
    user_last_name = data.get('user_last_name')
    
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
        #c.executemany("INSERT INTO producers VALUES (?,?,?);", many_customers)

        # c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('John', 'Elder', 'john@codem.com'))
        # c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('Alice', 'Elder', 'alice@codem.com'))
        # c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", ('Emma', 'Elder', 'emma@codem.com'))
        c.execute("SELECT count(*) FROM users WHERE first_name = user_first_name AND last_name = user_last_name AND email = user_email;")
        for record in c:
            if record[0] == 0:
                c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?);", user_first_name, user_last_name, user_email)
    
        c.execute("SELECT user_id FROM users WHERE first_name = user_first_name AND last_name = user_last_name AND email = user_email;")
        for record in c:
             = record[0]
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


@app.route('/new_product', methods=['POST'])
def add_product()->None:
    # Get data from request
    data = request.json
    
    # Extract email details
    user_id = data.get('user_id')
    product_name = data.get('product_name')
    amount = data.get('amount')
    unit_price = data.get('unit_price')
    product_addr = data.get('product_addr')
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

        # c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food1', 10, 11.1, '100 Queen Street', 1))
        # c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food2', 20, 22.2, '200 King Avenue', 2))
        # c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);", ('Food3', 30, 33.3, '300 Cat Boulevard', 3))
        c.execute("SELECT count(*) FROM users WHERE product_name = product_name AND amount = amount AND email = user_email;")
        for record in c:
            if record[0] == 0:

        c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?, ?);", product_name, amount, unit_price, product_addr, user_id)
        
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

# Emailing sending function (Winnie)

@app.route('/send_email', methods=['POST'])
def send_email():
    # Get data from request
    data = request.json
    
    # Extract email details
    user_email = data.get('user_email')
    product = data.get('product')
    farmer_name = data.get('farmer_name')
    farmer_email = data.get('farmer_email')
    
    
    subject = f"New Product Interests from {user_email}"
    body = f"""
<html>
    <head></head>
    <body style="font-family: 'Verdana', sans-serif;">
        <img src="https://img.clipart-library.com/24/41c926c5-f14e-4245-a6d6-909cf38e9a92.png" alt="Zero Waste Platform Logo">
        <p>Dear {farmer_name},</p>

        <p>I hope this message finds you well.</p>

        <p>As a representative of the <strong>Zero Waste Platform</strong>, I'm reaching out to you on behalf of one of our users, {user_email}, who has shown interest in your <strong>{product}</strong> listing. We greatly appreciate your dedication to reducing food waste by making your products available through our platform.</p>

        <p>Email: {user_email}, has expressed interest in purchasing your <strong>{product}</strong> and has asked me to facilitate communication between both parties. Could you please provide more details regarding the availability, pricing, and any specific pickup instructions or preferred times for the {product}?</p>

        <p>Thank you for your contribution to sustainability and for your commitment to reducing food waste. We value your partnership and look forward to connecting you with our user to facilitate the purchase of your <strong>{product}</strong>.</p>

        <p>Best regards,</p>
        <strong>Gaga Hsiang</strong><br>
        <strong>Representative of Zero Waste</strong><br>
        <strong>Zero Waste Platform</strong>
    </body>
</html>

    """

    # Email server configuration
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    email_username = 'winniehsiang1@gmail.com'  # Replace with your email
    email_password = 'mmplgecssojgizqq'  # Replace with your password

    # Create message
    msg = MIMEMultipart()
    msg['From'] = email_username
    msg['To'] = farmer_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    # Send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(email_username, email_password)
        server.sendmail(email_username, farmer_email, msg.as_string())

    return jsonify({'message': 'Email sent successfully'}), 200

@app.route('/get_data')
def get_data():
    try:
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Execute SQL query to retrieve data
        cursor.execute("SELECT name, location, price FROM your_table")
        
        # Fetch all rows from the result
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Convert data to list of dictionaries
        data_dict_list = []
        for row in data:
            data_dict_list.append({
                'name': row[0],
                'location': row[1],
                'price': row[2]
            })

        # Return data as JSON response
        return jsonify(data_dict_list)
    except sqlite3.Error as e:
        print("Database error:", e)
        return jsonify({'error': 'Database error'}), 500


# Search product by name (include database searching) (Jing)      
def setup() -> None:
    """Set up the testing environment for the database <dbname> using the
    username <username> and password <password> by importing the schema file
    at <schema_path> and the file containing the data at <data_path>.

    <schema_path> and <data_path> are the relative/absolute paths to the files
    containing the schema and the data respectively.
    """
    conn, c = None, None
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()


        # Create Tables
        c.execute("""CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name text NOT NULL,
                last_name text NOT NULL,
                email text NOT NULL
            );""")

        c.execute("""CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name text NOT NULL,
                amount INTEGER NOT NULL,
                price_per_unit REAL NOT NULL,
                product_address NOT NULL,
                user_id INTEGER NOT NULL REFERENCES users(user_id) ON DELETE CASCADE
            );""")

        conn.commit()

    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")

    finally:
        if c and not c.close:
            c.close()
        if conn and not conn.close:
            conn.close()

@app.route('/search', methods=['POST'])
def search():
    # Get data from request
    data = request.json
    
    # Extract email details
    product_name = data.get('product_name')

    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()

        # Execute SQL query to retrieve products' and producers' information
        c.execute("SELECT DISTINCT first_name, last_name, email, product_name, price_per_unit, amount FROM products NATURAL JOIN users WHERE product_name LIKE ?;", 
            ('%' + product_name + '%',))
        conn.commit()

        # Fetch all rows from the result
        data = c.fetchall()

        # Convert data to list of dictionaries
        data_dict_list = []
        for row in data:
            data_dict_list.append({
                'first_name': row[0],
                'last_name': row[1],
                'email': row[2],
                'product_name': row[3],
                'price_per_unit': row[4],
                'amount': row[5]
            })

        # Return data as JSON response
        return jsonify(data_dict_list)

    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")

    finally:
        if c and not c.close:
            c.close()
        if conn and not conn.close:
            conn.close()

# Run the Flask app
if __name__ == '__main__':
    setup()
    add_user()
    add_product()
    app.run(debug=True)

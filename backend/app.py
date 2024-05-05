from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from flask_cors import CORS, cross_origin

# Initialize the Flask app
app = Flask(__name__)

# initialize cors
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Define a route for the root URL
@app.route('/')
def index():
    return "Welcome to my Flask API agaerfddddddddfdadadadada!"


# Post Product function (Izabella)
@app.route('/new_product', methods=['POST'])
@cross_origin()
def add_product()->None:
    # Get data from request
    data = request.json
    
    # Extract data details
    product = data.get('product')
    quantity = data.get('quantity')
    price = data.get('price')
    location = data.get('location')
    description = data.get('description')
    user_email = data.get('farmer_email')
    user_name = data.get('farmer_name')
    image_link = data.get('image')

 
    conn, c = None, None
    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()
       
        c.execute("SELECT count(*) FROM users WHERE farmer_name == ? AND farmer_email == ?;", (user_name, user_email))
        for record in c:
            if record[0] == 0:
                c.execute("INSERT INTO users VALUES (NULL, ?, ?);", (user_name, user_email))
                
        c.execute("SELECT user_id FROM users WHERE farmer_name == ? AND farmer_email == ?;", (user_name, user_email))
        for record in c:
            user_id = record[0]

        c.execute("SELECT count(*) FROM products WHERE product == ? AND quantity == ? AND price  == ? AND location == ? AND user_id == ?;", (product, quantity, price, location, user_id))
        for record in c:
            if record[0] == 0:
                c.execute("INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?, ?, ?);", (product, quantity, price, location, description, image_link, user_id))

        conn.commit()

        return jsonify("Successfully Added")


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
@cross_origin()
def send_email():
    # Get data from request
    data = request.json
    print("Data", data)
    # Extract email details
    user_email = data.get('user_email')
    product = data.get('product')
    farmer_name = data.get('farmer_name')
    farmer_email = data.get('farmer_email')
    print(user_email, product, farmer_name, farmer_email)
    
    
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

@app.route('/get_data', methods=['POST'])
@cross_origin()
def get_data():
    try:
        # Connect to the database
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()

        # Execute SQL query to retrieve data
        cursor.execute("SELECT DISTINCT farmer_name, farmer_email, product, quantity, price, location, description, image FROM products NATURAL JOIN users")
        
        # Fetch all rows from the result
        data = cursor.fetchall()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        # Convert data to list of dictionaries
        data_dict_list = []
        for row in data:
            data_dict_list.append({
                'farmer_name': row[0],
                'farmer_email': row[1],
                'product': row[2],
                'quantity': row[3],
                'price': row[4],
                'location': row[5],
                'description': row[6],
                'image': row[7]
            })

        # Return data as JSON response
        return jsonify(data_dict_list)
        
    except sqlite3.Error as e:
        print("Database error:", e)
        return jsonify({'error': 'Database error'}), 500
    
    except Exception as ex:
        conn.rollback()
        raise Exception(f"Couldn't set up environment for tests: \n{ex}")


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
                farmer_name text NOT NULL,
                farmer_email text NOT NULL
            );""")

        c.execute("""CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY AUTOINCREMENT,
                product text NOT NULL,
                quantity text NOT NULL,
                price text NOT NULL,
                location text NOT NULL,
                description text,
                image text,
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
@cross_origin()
def search():
    
    # Get data from request
    data = request.json
    
    # Extract email details
    product = data.get('product')

    print("Data", data)
    print("Product", product)
    

    try:
        # Connect to database
        conn = sqlite3.connect('database.db')

        # Create a cursor
        c = conn.cursor()

        # Execute SQL query to retrieve products' and producers' information
        c.execute("SELECT DISTINCT farmer_name, farmer_email, product, quantity, price, location, description, image FROM products NATURAL JOIN users WHERE product LIKE ?;", 
            ('%' + product + '%',))
        conn.commit()

        # Fetch all rows from the result
        data = c.fetchall()

        # Convert data to list of dictionaries
        data_dict_list = []
        for row in data:
            data_dict_list.append({
                'farmer_name': row[0],
                'farmer_email': row[1],
                'product': row[2],
                'quantity': row[3],
                'price': row[4],
                'location': row[5],
                'description': row[6],
                'image': row[7]
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
    app.run(debug=True)




from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import DB_CONFIG
import datetime




app = Flask(__name__)
app.secret_key = 'secret_key'  # Add a secret key for flashing messages



@app.route('/')
def index():
    return render_template('index.html')

# Route to view products
@app.route('/products')
def view_products():
    try:
        connection = mysql.connector.connect(**DB_CONFIG) 
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
    except Exception as e:
        flash(f"Error fetching products: {e}", "danger")
        products = []
    finally:
        cursor.close()
        connection.close()
    return render_template('view_products.html', products=products)

# Route to add products
@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    connection = None
    cursor = None
    if request.method == 'POST':
        # Retrieve form data
            #product_id = request.form['product_id']
            product_name = request.form['product_name']
            category_id = request.form['category_id']
            supplier_id = request.form['supplier_id']
            
            unit_price = request.form['unit_price']
            units_in_stock = request.form['units_in_stock']
            

            print("Form data received:", request.form)

            # Connect to the database
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()
            query = """
                INSERT INTO Products (product_name, category_id, supplier_id, unit_price, units_in_stock)
                VALUES (%s,%s, %s, %s, %s)
            """
            values = (product_name, category_id, supplier_id, unit_price, units_in_stock)
            print("Executing query:", query, "with values:", values)
            
            print(request.form)  # Inspect all submitted form data
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return redirect(url_for('view_products'))
    return render_template('add_product.html')

        
        

        
            
    # Fetch suppliers for the dropdown in GET request
    '''try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT supplier_id, supplier_name FROM Suppliers")
        suppliers = cursor.fetchall()
    except Exception as e:
        print(f"Error fetching suppliers: {e}")
        flash(f"Error fetching suppliers: {e}", "danger")
        suppliers = []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()'''

    #return render_template('add_product.html', suppliers=suppliers)
# route for add_suppliers 
@app.route('/add_supplier', methods=['GET', 'POST'])

def add_supplier():
    connection = None
    cursor = None
    if request.method == 'POST':
        try:
            # Retrieve form data
            supplier_name = request.form['supplier_name']
            contact_name = request.form['contact_name']
            
            address = request.form['address']
            city = request.form['city']
            postal_code = request.form['postal_code']
            country = request.form['country']
            phone = request.form['phone']
            # Generate timestamps
            

            # Connect to the database

            print("Form data received:", supplier_name, contact_name, address, city, postal_code, country, phone)

            # Connect to the database
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor()
            query = """
                INSERT INTO Suppliers 
                (supplier_name, contact_name, address, city, postal_code, country, phone)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            values = (supplier_name, contact_name,  address, city, postal_code, country, phone)
            print("Executing query:", query, "with values:", values)
            
            cursor.execute(query, values)
            connection.commit()  # Ensure changes are committed
            print("Supplier added successfully!")
            flash("Supplier added successfully!", "success")
        except Exception as e:
            print(f"Error during supplier insertion: {e}")
            flash(f"Error adding supplier: {e}", "danger")
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()
        return redirect(url_for('view_suppliers'))

    return render_template('add_supplier.html')
    
    

# Route to manage products
@app.route('/manage_products')
def manage_products():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Products")
        products = cursor.fetchall()
    except Exception as e:
        flash(f"Error fetching products for management: {e}", "danger")
        products = []
    finally:
        cursor.close()
        connection.close()
    return render_template('manage_products.html', products=products)

# Route to view suppliers
@app.route('/suppliers')
def view_suppliers():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Suppliers")
        suppliers = cursor.fetchall()
    except Exception as e:
        flash(f"Error fetching suppliers: {e}", "danger")
        suppliers = []
    finally:
        cursor.close()
        connection.close()
    return render_template('view_supplier.html', suppliers=suppliers)

# Route to view orders
@app.route('/orders')
def view_orders():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Orders")
        orders = cursor.fetchall()
    except Exception as e:
        flash(f"Error fetching orders: {e}", "danger")
        orders = []
    finally:
        cursor.close()
        connection.close()
    return render_template('view_orders.html', orders=orders)

# Route to view customers
@app.route('/customers')
def view_customers():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        #print(customers)
    except Exception as e:
        flash(f"Error fetching customers: {e}", "danger")
        customers = []
        
    finally:
        cursor.close()
        connection.close()
    return render_template('view_customers.html', customers=customers)

# Route to view warehouses
@app.route('/warehouses')
def view_warehouses():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Warehouses")
        warehouses = cursor.fetchall()
    except Exception as e:
        flash(f"Error fetching warehouses: {e}", "danger")
        warehouses = []
    finally:
        cursor.close()
        connection.close()
    return render_template('view_warehouses.html', warehouses=warehouses)

# Route to view transactions
@app.route('/inventorytransactions')
def view_transactions():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT *FROM inventorytransactions")
        inventorytransactions = cursor.fetchall()
        #print(inventorytransactions)
    except Exception as e:
        flash(f"Error fetching transactions: {e}", "danger")
        transactions = []
    finally:
        cursor.close()
        connection.close()
    return render_template('view_transactions.html',inventorytransactions=inventorytransactions)


@app.route('/billing', methods=['GET', 'POST'])
def billing():
    try:
        # Connect to the database and fetch products
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT product_id, product_name, unit_price FROM products')
        products = cursor.fetchall()
        cursor.close()
        connection.close()

        # Initialize the cart and total price
        cart = []
        total_price = 0

        if request.method == 'POST':
            # Retrieve cart data from hidden input fields
            cart_data = request.form.getlist('cart')
            for item in cart_data:
                product_id, product_name, unit_price, quantity = item.split('|')
                cart.append({
                    'product_id': int(product_id),
                    'product_name': product_name,
                    'unit_price': float(unit_price),
                    'quantity': int(quantity),
                })

            # Handle actions: Add or Remove products
            action = request.form.get('action')
            product_id = int(request.form.get('product', 0))
            quantity = int(request.form.get('quantity', 1))

            if action == 'add':
                # Add product to cart
                product = next((p for p in products if p['product_id'] == product_id), None)
                if product:
                    cart.append({
                        'product_id': product['product_id'],
                        'product_name': product['product_name'],
                        'unit_price': product['unit_price'],
                        'quantity': quantity,
                    })

            elif action == 'remove':
                # Remove product from cart
                cart = [item for item in cart if item['product_id'] != product_id]

            # Calculate total price
            total_price = sum(item['unit_price'] * item['quantity'] for item in cart)

        # Render the billing page
        return render_template('billing.html', products=products, cart=cart, total_price=total_price)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "An error occurred while processing your request.", 500
    

@app.route('/receipt', methods=['GET', 'POST'])
def receipt():
    try:
        # Connect to the database
        connection = mysql.connector.connect(**DB_CONFIG)
        cursor = connection.cursor(dictionary=True)

        # Fetch products from the database for the dropdown
        cursor.execute('SELECT product_id, product_name, unit_price FROM products')
        products = cursor.fetchall()
        
        cursor.close()
        connection.close()

        # Initialize variables
        selected_products = []
        receipt = ""
        total_price = 0

        if request.method == 'POST':
            # Get selected product IDs from the form
            selected_product_ids = request.form.getlist('products')

            # Generate receipt
            receipt = "Receipt:\n"
            receipt += "-" * 30 + "\n"

            # Reconnect to the database to fetch selected product details
            connection = mysql.connector.connect(**DB_CONFIG)
            cursor = connection.cursor(dictionary=True)

            for product_id in selected_product_ids:
                cursor.execute('SELECT * FROM products WHERE product_id = %s', (product_id,))
                product = cursor.fetchone()
                if product:
                    selected_products.append(product)
                    receipt += f"{product['product_name']}: ${product['unit_price']}\n"
                    total_price += product['unit_price']

            cursor.close()
            connection.close()

            receipt += "-" * 30 + "\n"
            receipt += f"Total Price: ${total_price}\n"

        return render_template('receipt.html', products=products, receipt=receipt, total_price=total_price)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return "An error occurred while processing your request.", 500



if __name__ == '__main__':
    app.run(debug=True)




import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="supermarket"
    )
    return connection

import streamlit as st


# Streamlit App Configuration
st.set_page_config(page_title="Supermarket Inventory Management", layout="wide")

# Title
st.title("Supermarket Inventory Management System")

# Sidebar Navigation
menu = st.sidebar.selectbox(
    "Menu",
    ["View Products", "Add Product", "View Suppliers", "Add Supplier", "View Orders", "View Warehouses"]
)

# Function to Fetch Data
def fetch_data(query):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# Function to Modify Data
def modify_data(query, values):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(query, values)
    conn.commit()
    cursor.close()
    conn.close()

# View Products
if menu == "View Products":
    st.subheader("Products List")
    query = "SELECT * FROM Products"
    products = fetch_data(query)
    st.write(products)

# Add Product
elif menu == "Add Product":
    st.subheader("Add a New Product")
    product_name = st.text_input("Product Name")
    category_id = st.number_input("Category ID", step=1)
    supplier_id = st.number_input("Supplier ID", step=1)
    unit_price = st.number_input("Unit Price", step=0.01)
    units_in_stock = st.number_input("Units in Stock", step=1)

    if st.button("Add Product"):
        query = """
            INSERT INTO Products (product_name, category_id, supplier_id, unit_price, units_in_stock)
            VALUES (%s, %s, %s, %s, %s)
        """
        values = (product_name, category_id, supplier_id, unit_price, units_in_stock)
        modify_data(query, values)
        st.success(f"Product '{product_name}' added successfully!")

# View Suppliers
elif menu == "View Suppliers":
    st.subheader("Suppliers List")
    query = "SELECT * FROM Suppliers"
    suppliers = fetch_data(query)
    st.write(suppliers)

# Add Supplier
elif menu == "Add Supplier":
    st.subheader("Add a New Supplier")
    supplier_name = st.text_input("Supplier Name")
    contact_name = st.text_input("Contact Name")
    address = st.text_input("Address")
    city = st.text_input("City")
    postal_code = st.text_input("Postal Code")
    country = st.text_input("Country")
    phone = st.text_input("Phone Number")

    if st.button("Add Supplier"):
        query = """
            INSERT INTO Suppliers (supplier_name, contact_name, address, city, postal_code, country, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (supplier_name, contact_name, address, city, postal_code, country, phone)
        modify_data(query, values)
        st.success(f"Supplier '{supplier_name}' added successfully!")

# View Orders
elif menu == "View Orders":
    st.subheader("Orders List")
    query = "SELECT * FROM Orders"
    orders = fetch_data(query)
    st.write(orders)

# View Warehouses
elif menu == "View Warehouses":
    st.subheader("Warehouses List")
    query = "SELECT * FROM Warehouses"
    warehouses = fetch_data(query)
    st.write(warehouses)

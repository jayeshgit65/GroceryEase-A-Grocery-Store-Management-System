# Grocery Management System

A comprehensive web-based grocery store management application built with a 3-tier architecture for efficient inventory and order management.

## Features

- **Product Management**: Add, view, and delete grocery products
- **Order Management**: Create and track customer orders
- **Inventory Control**: Manage product quantities and units of measurement
- **Responsive UI**: Clean, user-friendly interface with Bootstrap styling

## Architecture

**3-Tier Application Structure:**
1. **Frontend**: HTML/CSS/JavaScript/Bootstrap
2. **Backend**: Python Flask REST API
3. **Database**: MySQL

## Database Schema

The application uses 4 main tables:

### 1. products
```sql
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
);
```

### 2. uom (Unit of Measurement)
```sql
CREATE TABLE uom (
    uom_id INT AUTO_INCREMENT PRIMARY KEY,
    uom_name VARCHAR(45) NOT NULL
);
```

### 3. orders
```sql
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    total DECIMAL(10,2) NOT NULL,
    datetime DATETIME NOT NULL
);
```

### 4. order_details
```sql
CREATE TABLE order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DECIMAL(10,2) NOT NULL,
    total_price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);
```

**Relationships:**
- `products.uom_id` → `uom.uom_id` (Many-to-One)
- `order_details.order_id` → `orders.order_id` (Many-to-One)
- `order_details.product_id` → `products.product_id` (Many-to-One)

## Project Structure

```
Grocery_Management_System/
├── backend/
│   ├── server.py           # Flask application server
│   ├── products_dao.py     # Product data access operations
│   ├── orders_dao.py       # Order data access operations
│   ├── uom_dau.py         # Unit of measurement operations
│   └── sql_connection.py   # Database connection handler
├── ui/
│   ├── css/               # Stylesheets
│   ├── js/                # JavaScript files
│   ├── images/            # Static images
│   ├── index.html         # Dashboard page
│   ├── manage-product.html # Product management page
│   └── order.html         # Order management page
├── requirements.txt       # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.7+
- MySQL Server
- Web browser

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/jayeshgit65/GroceryEase-A-Grocery-Store-Management-System.git
cd GroceryEase-A-Grocery-Store-Management-System
```

### 2. Install MySQL
Download and install MySQL for Windows: https://dev.mysql.com/downloads/installer/

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
1. Create a MySQL database named `grocery_store`
2. Update database connection details in `backend/sql_connection.py`:
   ```python
   __cnx = mysql.connector.connect(
       user='your_username', 
       password='your_password',
       host='127.0.0.1',
       database='grocery_store'
   )
   ```
3. Create the required tables using the SQL schema provided above

### 5. Run the Application
```bash
cd backend
python server.py
```

The Flask server will start on `http://localhost:5000`

### 6. Access the Frontend
Open `ui/index.html` in your web browser to access the application.

## API Endpoints

- `GET /getProducts` - Retrieve all products
- `GET /getUOM` - Get units of measurement
- `POST /insertProduct` - Add new product
- `POST /deleteProduct` - Delete a product
- `GET /getAllOrders` - Retrieve all orders
- `POST /insertOrder` - Create new order

## Usage

1. **Dashboard**: View system overview and navigate to different modules
2. **Manage Products**: Add, view, and delete grocery products
3. **Orders**: Create and manage customer orders

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Database**: MySQL
- **Libraries**: mysql-connector-python

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Notes

- Update database credentials in `backend/sql_connection.py` before running
- Ensure MySQL server is running on localhost:3306
- Frontend files are served statically - open HTML files directly in browser
